from manim import *

class DeepSpeedZeROAnimation(Scene):
    def construct(self):
        title = Text("DeepSpeed ZeRO-3 & NVMe Memory Partitioning", font_size=30, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))

        vram = Rectangle(width=3.5, height=2, color=BLUE).shift(LEFT * 4)
        vram_txt = Text("GPU VRAM\n(Active Layers)", font_size=16).move_to(vram)

        ram = Rectangle(width=3.5, height=2, color=ORANGE).shift(ORIGIN)
        ram_txt = Text("Host CPU RAM\n(Optimizer States)", font_size=16).move_to(ram)

        nvme = Rectangle(width=3.5, height=2, color=PURPLE).shift(RIGHT * 4)
        nvme_txt = Text("PCIe NVMe\n(70B Parameters)", font_size=16).move_to(nvme)

        a1 = Arrow(vram.get_right(), ram.get_left(), color=YELLOW)
        a2 = Arrow(ram.get_right(), nvme.get_left(), color=YELLOW)

        self.play(Create(vram), Write(vram_txt))
        self.play(GrowArrow(a1), Create(ram), Write(ram_txt))
        self.play(GrowArrow(a2), Create(nvme), Write(nvme_txt))
        self.wait(1)
