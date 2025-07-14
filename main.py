from core.agent import generate_command
from core.executor import run_command
from core.memory import save_history, view_history, clear_history
from core.intent import map_intent_to_command
from core.explainer import explain_command
from core.settings import load_settings, toggle_autorun
from core.error_explainer import explain_error
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

last_prompt = ""
settings = load_settings()

def main():
    global last_prompt
    print("[bold cyan]🤖 Welcome to Termi — your AI terminal assistant![/bold cyan]")

    while True:
        try:
            prompt = Prompt.ask("\n📜 Prompt (natural language or shell task)").strip()
            mapped = map_intent_to_command(prompt)

            if mapped == "/exit":
                print("[bold red] Goodbye![/bold red]")
                break

            elif mapped == "/history":
                history = view_history()
                if not history:
                    print("[yellow]⚠️ No history found.[/yellow]")
                for h in history[-10:]:
                    print(f"[green]{h['timestamp']}[/green] :: [yellow]{h['prompt']}[/yellow] → [white]{h['command']}[/white]")
                continue

            elif mapped == "/clearhistory":
                clear_history()
                print("[bold red]🧹 History cleared.[/bold red]")
                continue

            elif prompt.startswith("/autorun"):
                if "on" in prompt:
                    toggle_autorun(True)
                    print("[green]⚙️ Autorun mode ENABLED.[/green]")
                else:
                    toggle_autorun(False)
                    print("[red]🛑 Autorun mode DISABLED.[/red]")
                settings.update(load_settings())
                continue

            elif prompt == "/retry":
                if not last_prompt:
                    print("[yellow]⚠️ No command to retry.[/yellow]")
                    continue
                prompt = last_prompt

            elif prompt.lower().startswith("explain") or "what does" in prompt.lower() or "describe" in prompt.lower():
                explanation = explain_command(prompt)
                print(Panel(explanation, title="📘 Explanation"))
                continue

            command = generate_command(prompt)
            last_prompt = prompt  
            print(Panel(f"[bold yellow]{command}[/bold yellow]", title="💡 Suggested Command"))

            run_cmd = False
            if settings["autorun"]:
                run_cmd = True
            else:
                edit = Prompt.ask("Do you want to edit this command before running?", choices=["y", "n"], default="n")
                if edit.lower() == "y":
                    command = Prompt.ask("✏️ Edit command", default=command)

                confirm = Prompt.ask("Run it?", choices=["y", "n"], default="n")
                run_cmd = confirm == "y"

            if run_cmd:
                output, error = run_command(command)
                if output:
                    print(Panel(output.strip(), title="✅ Output", style="green"))
                if error:
                    print(Panel(error.strip(), title="❌ Error", style="red"))
                    fix = explain_error(error)
                    print(Panel(fix, title="🧠 Error Explanation", style="magenta"))
                save_history(prompt, command)

        except KeyboardInterrupt:
            print("\n[bold red]⛔ Use /exit to quit Termi safely.[/bold red]")
            continue
        except Exception as e:
            print(f"[bold red]❌ Unexpected error: {str(e)}[/bold red]")
            continue

if __name__ == "__main__":
    main()
