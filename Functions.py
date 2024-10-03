import os
from colorama import Fore
import time
import psutil
import subprocess


blue = Fore.BLUE
white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

normal_content = "module.exports = require('./core.asar');"

def kill_discord():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and 'discord' in proc.info['name'].lower():
            proc.kill()

def restart_discord(latest_app_path, version):
    discord_exe = {
        "Discord": os.path.join(latest_app_path, "Discord.exe"),
        "DiscordCanary": os.path.join(latest_app_path, "DiscordCanary.exe"),
        "DiscordPTB": os.path.join(latest_app_path, "DiscordPTB.exe")
    }

    if version in discord_exe and os.path.exists(discord_exe[version]):
        exe_path = discord_exe[version]
        subprocess.Popen(
            [exe_path],
            creationflags=subprocess.CREATE_NO_WINDOW,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

def check_injection(content):
    return content != normal_content


def check_clean_discord():
    main = os.path.basename(os.path.expanduser("~"))
    
    discord_paths = {
        "Discord": f"C:\\Users\\{main}\\AppData\\Local\\Discord\\",
        "DiscordCanary": f"C:\\Users\\{main}\\AppData\\Local\\DiscordCanary\\",
        "DiscordPTB": f"C:\\Users\\{main}\\AppData\\Local\\DiscordPTB\\"
    }

    for version, path in discord_paths.items():
        if os.path.exists(path):
            print(f"[{green}ENCONTRADO{white}] Caminho encontrado para {blue + version}.{white}")
            print(f"[{green}INICIANDO{white}] Iniciando a verificação de injeções...\n")
            time.sleep(1)
            
            app_folders = [d for d in os.listdir(path) if d.startswith("app-")]

            if app_folders:
                latest_app = max(app_folders, key=lambda x: x.split("-")[1])
                latest_app_path = os.path.join(path, latest_app)
                modules_path = os.path.join(latest_app_path, "modules")
                
                if os.path.exists(modules_path):
                    core_folders = [d for d in os.listdir(modules_path) if d.startswith("discord_desktop_core")]

                    if core_folders:
                        latest_core_folder = max(core_folders)
                        index_js_path = os.path.join(modules_path, latest_core_folder, "discord_desktop_core", "index.js")
                        print(f"[{green}CAMINHO DO INDEX{white}] {index_js_path}\n")
                        print(f"[{green}VERIFICANDO{white}] Verificando se foi injetado algo...")
                        time.sleep(1)
                        
                        with open(index_js_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                        
                        if check_injection(content):
                            print(f"[{red}INJEÇÃO ENCONTRADA{white}] Possível injeção encontrada.\n")
                            dump_choice = input(f"[{blue}SALVAR{white}] Deseja salvar o arquivo? (yes ou 'Enter' para pular): ").strip().lower()
                            
                            if dump_choice == "yes":
                                dump_filename = input(f"[{blue}ARQUIVO{white}] Informe o nome do arquivo: ").strip()
                                dump_filename = f"{dump_filename}.js"
                                with open(dump_filename, 'w', encoding='utf-8') as dump_file:
                                    dump_file.write(content)
                                print(f"[{green}SALVO{white}] Arquivo salvo com sucesso como {dump_filename} no diretório atual.\n")
                            
                            print(f"[{green}LIMPANDO{white}] Limpando o arquivo, por favor, aguarde...")
                            time.sleep(2)
                            with open(index_js_path, 'w', encoding='utf-8') as file:
                                file.write(normal_content)
                            print(f"[{green}SEGURO{white}] Possível injeção removida com sucesso.\n")
                            print(f"[{green}REINICIANDO{white}] Reiniciando {version} para aplicar as mudanças...")
                            print("""
------------------------------------------------------------------------
""")

                            kill_discord()
                            restart_discord(latest_app_path, version)
                        else:
                            print(f"[{green}SEGURO{white}] Nenhuma injeção detectada.")
                            print("""
------------------------------------------------------------------------
""")
                    else:
                        print(f"[{red}ERRO{white}] Pasta Core não encontrada em {version}.")
                        print("""
------------------------------------------------------------------------
""")
                else:
                    print(f"[{red}ERRO{white}] Pasta Modules não encontrada em {version}.")
                    print("""
------------------------------------------------------------------------
""")
            else:
                print(f"[{red}ERRO{white}] Pasta App não encontrada em {version}.")
                print("""
------------------------------------------------------------------------
""")

def check_injection_discord():
    main = os.path.basename(os.path.expanduser("~"))
    
    discord_paths = {
        "Discord": f"C:\\Users\\{main}\\AppData\\Local\\Discord\\",
        "DiscordCanary": f"C:\\Users\\{main}\\AppData\\Local\\DiscordCanary\\",
        "DiscordPTB": f"C:\\Users\\{main}\\AppData\\Local\\DiscordPTB\\"
    }

    for version, path in discord_paths.items():
        if os.path.exists(path):
            print(f"[{green}ENCONTRADO{white}] Caminho encontrado para {blue + version}.{white}")
            print(f"[{green}INICIANDO{white}] Iniciando a verificação de injeções...\n")
            time.sleep(1)
            
            app_folders = [d for d in os.listdir(path) if d.startswith("app-")]

            if app_folders:
                latest_app = max(app_folders, key=lambda x: x.split("-")[1])
                latest_app_path = os.path.join(path, latest_app)
                modules_path = os.path.join(latest_app_path, "modules")
                
                if os.path.exists(modules_path):
                    core_folders = [d for d in os.listdir(modules_path) if d.startswith("discord_desktop_core")]

                    if core_folders:
                        latest_core_folder = max(core_folders)
                        index_js_path = os.path.join(modules_path, latest_core_folder, "discord_desktop_core", "index.js")
                        print(f"[{green}CAMINHO DO INDEX{white}] {index_js_path}\n")
                        print(f"[{green}VERIFICANDO{white}] Verificando se foi injetado algo...")
                        time.sleep(1)
                        
                        with open(index_js_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                        
                        if check_injection(content): 
                            print(f"[{red}INJEÇÃO ENCONTRADA{white}] Possível injeção encontrada.\n")
                            dump_choice = input(f"[{blue}SALVAR{white}] Deseja salvar o arquivo? (yes ou 'Enter' para pular): ").strip().lower()
                            
                            if dump_choice == "yes":
                                dump_filename = input(f"[{blue}ARQUIVO{white}] Informe o nome do arquivo: ").strip()
                                dump_filename = f"{dump_filename}.js"
                                with open(dump_filename, 'w', encoding='utf-8') as dump_file:
                                    dump_file.write(content)
                                print(f"[{green}SALVO{white}] Arquivo salvo com sucesso como {dump_filename} no diretório atual.\n")
                        else:
                            print(f"[{green}SEGURO{white}] Nenhuma injeção detectada.")
                            print("""
------------------------------------------------------------------------
""")
                    else:
                        print(f"[{red}ERRO{white}] Pasta Core não encontrada em {version}.")
                        print("""
------------------------------------------------------------------------
""")
                else:
                    print(f"[{red}ERRO{white}] Pasta Modules não encontrada em {version}.")
                    print("""
------------------------------------------------------------------------
""")
            else:
                print(f"[{red}ERRO{white}] Pasta App não encontrada em {version}.")
                print("""
------------------------------------------------------------------------
""")

def clean_discord_version(version):
    main = os.path.basename(os.path.expanduser("~"))
    
    discord_paths = {
        "1": ("Discord", f"C:\\Users\\{main}\\AppData\\Local\\Discord\\"),
        "2": ("DiscordCanary", f"C:\\Users\\{main}\\AppData\\Local\\DiscordCanary\\"),
        "3": ("DiscordPTB", f"C:\\Users\\{main}\\AppData\\Local\\DiscordPTB\\")
    }
    
    if version in discord_paths:
        version_name, path = discord_paths[version]
        
        if os.path.exists(path):
            print(f"[{green}ENCONTRADO{white}] Caminho encontrado para {blue + version_name}.{white}")
            print(f"[{green}INICIANDO{white}] Processo de limpeza para {version_name}...\n")
            time.sleep(1)
            
            app_folders = [d for d in os.listdir(path) if d.startswith("app-")]

            if app_folders:
                latest_app = max(app_folders, key=lambda x: x.split("-")[1])
                latest_app_path = os.path.join(path, latest_app)
                modules_path = os.path.join(latest_app_path, "modules")
                
                if os.path.exists(modules_path):
                    core_folders = [d for d in os.listdir(modules_path) if d.startswith("discord_desktop_core")]

                    if core_folders:
                        latest_core_folder = max(core_folders)
                        index_js_path = os.path.join(modules_path, latest_core_folder, "discord_desktop_core", "index.js")
                        print(f"[{green}CAMINHO DO INDEX{white}] {index_js_path}\n")
                        print(f"[{green}VERIFICANDO{white}] Verificando se foi injetado algo...")
                        time.sleep(1)
                        
                        with open(index_js_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                        
                        if check_injection(content):
                            print(f"[{red}INJEÇÃO ENCONTRADA{white}] Possível injeção encontrada.\n")
                            dump_choice = input(f"[{blue}SALVAR{white}] Deseja salvar o arquivo? (yes ou 'Enter' para pular): ").strip().lower()
                            
                            if dump_choice == "yes":
                                dump_filename = input(f"[{blue}ARQUIVO{white}] Informe o nome do arquivo: ").strip()
                                dump_filename = f"{dump_filename}.js"
                                with open(dump_filename, 'w', encoding='utf-8') as dump_file:
                                    dump_file.write(content)
                                print(f"[{green}SALVO{white}] Arquivo salvo com sucesso como {dump_filename} no diretório atual.\n")
                            
                            print(f"[{green}LIMPANDO{white}] Limpando o arquivo, por favor, aguarde...")
                            time.sleep(2)
                            with open(index_js_path, 'w', encoding='utf-8') as file:
                                file.write(normal_content)
                            print(f"[{green}SEGURO{white}] Possível injeção removida com sucesso.\n")
                            print(f"[{green}REINICIANDO{white}] Reiniciando {version_name} para aplicar as mudanças...")
                            print("""
------------------------------------------------------------------------
""")

                            kill_discord()
                            restart_discord(latest_app_path, version_name)
                        else:
                            print(f"[{green}SEGURO{white}] Nenhuma injeção detectada.")
                            print("""
------------------------------------------------------------------------
""")
                    else:
                        print(f"[{red}ERRO{white}] Pasta Core não encontrada em {version_name}.")
                        print("""
------------------------------------------------------------------------
""")
                else:
                    print(f"[{red}ERRO{white}] Pasta Modules não encontrada em {version_name}.")
                    print("""
------------------------------------------------------------------------
""")
            else:
                print(f"[{red}ERRO{white}] Pasta App não encontrada em {version_name}.")
                print("""
------------------------------------------------------------------------
""")

           
help = f"""                     [{blue}MENU DE AJUDA{white}] 

[{blue}DESENVOLVEDOR{white}] uxie
[{blue}GITHUB{white}] https://github.com/theuxieofc

[{blue}VERIFICAR INJEÇÕES{white}] Este script irá inspecionar o índice do Discord para analisar se algum código malicioso foi injetado nele.
[{blue}LIMPAR INJEÇÕES{white}] Este script irá limpar o índice do Discord para remover qualquer código malicioso que tenha sido injetado.

[{red}AVISO{white}] Se roubado, lembre-se de usar este script para remover possíveis injeções do Discord e verificar se há algum subprocesso em execução.
"""
