import typer
import ast
from typing import List

from Modules.lab4 import linearize_iter, linearize_rec, calc_ab_iter, calc_ab_rec
from Modules.lab5 import make_averager
from Modules.lab6 import apply_func_n_times

app = typer.Typer()

@app.command("lab4-linearize")
def run_lab4_linearize(data_str: str = typer.Argument(..., help="String representation of the list"), method: str = typer.Option("iter", "--method", "-m", help="Method: iter or rec")):
    try:
        data_list = ast.literal_eval(data_str)
    except Exception:
        typer.echo("Error: Invalid list format.")
        raise typer.Exit(code=1)

    if method == "iter":
        result = linearize_iter(data_list)
    elif method == "rec":
        result = linearize_rec(data_list)
    else:
        typer.echo("Error: Unknown method. Use 'iter' or 'rec'.")
        raise typer.Exit(code=1)
    
    typer.echo(result)

@app.command("lab4-calc-ab")
def run_lab4_calc_ab(k: int = typer.Argument(..., help="Index k")):
    if k < 1:
        typer.echo("Error: k must be >= 1")
        raise typer.Exit(code=1)
    
    res_iter = calc_ab_iter(k)
    res_rec = calc_ab_rec(k)
    typer.echo(f"Iterative: {res_iter}, Recursive: {res_rec}")

@app.command("lab5-averager")
def run_lab5_averager(values: List[float] = typer.Option(..., "--value", "-v", help="Values to average")):
    if not values:
        typer.echo("Error: No values provided.")
        raise typer.Exit(code=1)
        
    avg_func = make_averager()
    results = []
    for val in values:
        current_avg = avg_func(val)
        results.append(current_avg)
    
    typer.echo(results)

@app.command("lab6-apply")
def run_lab6_apply(sequence: List[float] = typer.Option(..., "--seq", "-s", help="Input sequence"), func_name: str = typer.Option("square", "--func", "-f", help="Function name: square, double, increment"), n: int = typer.Option(1, "--times", "-n", help="Number of times to apply")):
    funcs = {
        "square": lambda x: x ** 2,
        "double": lambda x: x * 2,
        "increment": lambda x: x + 1
    }
    
    if func_name not in funcs:
        typer.echo(f"Error: Unknown function '{func_name}'. Available: square, double, increment")
        raise typer.Exit(code=1)
        
    func = funcs[func_name]
    result = list(apply_func_n_times(sequence, func, n))
    typer.echo(result)

if __name__ == "__main__":
    app()