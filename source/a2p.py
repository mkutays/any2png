import click
import json
from plotly import express as px

import pandas as pd


def read_json_data(fjson):
    with open(fjson, "r") as fjs:
        data = json.load(fjs)
    df = pd.DataFrame(list(zip(data["X"], data["Y"])), columns=['X', 'Y'])
    return df


def draw_plot(df, width, height):
    fig = px.line(df, x="X", y="Y", width=width, height=height)
    fig.update_traces(line_color='#d602ee', line_width=3)
    fig.update_xaxes(tickfont=dict(family='Rockwell', color='white', size=12))
    fig.update_yaxes(tickfont=dict(family='Rockwell', color='white', size=12))
    fig.update_layout({"plot_bgcolor": "rgba(66, 66, 66, 100)",
                       "paper_bgcolor": "rgba(66, 66, 66, 100)",
                       })
    img = fig.to_image(format="png")
    return img


def export_png(img, fout):
    with open(fout, "wb") as out:
        out.write(img)


@click.command()
@click.option("--fjson", default='din.json', help="Number of greetings.")
@click.option('--width', default=1000, help='Image width')
@click.option('--height', default=600, help='Image heigth')
@click.option('--fout', default='dout.png', help='Output file path')
def cli(fjson, width, height, fout):
    df = read_json_data(fjson)
    img = draw_plot(df, width, height)
    export_png(img, fout)


def qwe():
    print("qwe")


if __name__ == "__main__":
    qwe()
