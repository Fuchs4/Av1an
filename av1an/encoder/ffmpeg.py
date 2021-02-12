import os
import re

from av1an.project import Project
from av1an.chunk import Chunk
from av1an.commandtypes import MPCommands, CommandPair, Command
from av1an.encoder.encoder import Encoder
from av1an.utils import list_index_of_regex, terminate


class Ffmpeg(Encoder):
    def __init__(self):
        super().__init__(encoder_bin='ffmpeg',
                         encoder_help='ffmpeg --help',
                         default_args=[
                            '-c:v', 'libaom-av1', '-threads=8', '-cpu-used=6',
                            '-b:v', '0', '-crf', '30'
                            '-tile-columns=2', '-tile-rows=1'
                         ],
                         default_passes=2,
                         default_q_range=(15, 55),
                         output_extension='mkv')

    def compose_1_pass(self, a: Project, c: Chunk, output: str) -> MPCommands:
        return [
            CommandPair(
                Encoder.compose_ffmpeg_pipe(a),
                ['ffmpeg', '-i', '-', *a.video_params, output])
        ]

    def compose_2_pass(self, a: Project, c: Chunk, output: str) -> MPCommands:
        return [
            CommandPair(Encoder.compose_ffmpeg_pipe(a), [
                'ffmpeg', '-i', '-', '-pass', '1', *a.video_params,
                '-loglevel', 'warning',
                f'-passlogfile {c.fpf}.log', '-f', 'null', os.devnull
            ]),
            CommandPair(Encoder.compose_ffmpeg_pipe(a), [
                'ffmpeg', '-i', '-', '-pass', '2', *a.video_params,
                f'-passlogfile {c.fpf}.log', output
            ])
        ]

    def man_q(self, command: Command, q: int) -> Command:
        """Return command with new cq value"""

        adjusted_command = command.copy()

        i = list_index_of_regex(adjusted_command, r"-crf")
        adjusted_command[i + 1] = f'{q}'

        return adjusted_command

    def match_line(self, line: str):
        """Extract number of encoded frames from line.

        :param line: one line of text output from the encoder
        :return: match object from re.search matching the number of encoded frames"""

        if 'ERROR' in line.lower():
            print('\n\nERROR IN ENCODING PROCESS\n\n', line)
            terminate()
        return re.search(r"frame=\s*([0-9]+)\s", line)
