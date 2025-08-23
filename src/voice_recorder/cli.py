import os
import time
import click
from rich.console import Console
from rich.table import Table
from .recorder import record_wav, list_devices

back_record = ["soundfile", "wavio", "scipy"]
console = Console()


@click.group(help="Voice Recorder CLI")
def app():
    pass


@app.command()
@click.option(
    "--output",
    "-o",
    type=click.Path(dir_okay=False),
    default="recordings/out.wav",
    show_default=True,
)
@click.option("--duration", "-d", type=float, required=True, help="Duration in second")
@click.option("--samplerate", type=int, default=44100, show_default=True)
@click.option("--channels", "-c", type=int, default=1, show_default=True)
@click.option("--device", type=int, default=None, help="Input device id (see 'device')")
@click.option(
    "--backend", type=click.Choice(back_record), default="soundfile", show_default=True
)
def record(
    output: str,
    duration: float,
    samplerate: int,
    channels: int,
    device: int | None,
    backend: str,
):
    os.makedirs(os.path.dirname(output), exist_ok=True)
    console.rule("RECORDING")
    console.print(f"Saving to: [bold]{output}[/bold] (recording using: {backend})")
    start = time.time()

    record_wav(output, duration, samplerate, channels, device, backend)
    console.print(f"Done in {time.time()-start:.2f}s", style="green")


@app.command()
def devices():
    data = list_devices()

    if not data:
        console.print("No Input device found.", style="red")
        return
    table = Table(title="\n Input Devices")
    table.add_column("ID", justify="right")
    table.add_column("DEVICE NAME", justify="center")
    table.add_column("CHANNELS", justify="right")
    table.add_column("DEFAULT SR (Hz)", justify="right")

    for d in data:
        table.add_row(
            str(d["id"]), d["name"], str(d["channels"]), str(d["default_samplerate"])
        )
    console.print(table)
    print()
