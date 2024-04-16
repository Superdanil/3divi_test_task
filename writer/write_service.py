from datetime import datetime

from schemas import Req, ReqLine
from settings import Settings


class WriteService:
    """Класс записи файлов txt1 и txt2."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def write_txt1(self, req: ReqLine) -> str:
        """Записывает файл txt1."""
        str_ = f"| {req.request_id} | {req.time} | {datetime.now()} |\n"

        with open(self.settings.txt1_path, "r") as f:
            contents = f.readlines()

        contents_length = len(contents)

        if contents_length > req.line_number:
            contents[req.line_number - 1] = str_
        else:
            delta = req.line_number - contents_length
            appending_strings = ["\n" for _ in range(delta - 1)]
            appending_strings.append(str_)
            contents.extend(appending_strings)
        with open(self.settings.txt1_path, "w", encoding="utf-8") as file:
            file.writelines(contents)
        return str_

    def write_txt2(self, req: Req) -> dict[str, int]:
        """Записывает файл txt2."""
        with open(self.settings.txt2_path, "a", encoding="utf-8") as file:
            str_ = f"| {req.request_id} | {req.time} |\n"
            file.write(str_)
        with open(self.settings.txt2_path, "rb") as f:
            num_lines = sum(1 for _ in f)
        return {"line_number": num_lines}
