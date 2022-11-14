from pathlib import Path
from pdf2image import convert_from_path

pdf_path = Path("./pdf/Catalogue.pdf")
img_path = Path("./image")


def main():

    convert_from_path(
        pdf_path,
        first_page=1,
        last_page=1,
        dpi=200,
        fmt="jpeg",
        jpegopt={"quality": 100, "optimize": True, "progressive": False},
        output_folder=img_path,
        output_file=pdf_path.stem,
        size=(210, 297),
    )


# if __name__ == "__main__":
main()
