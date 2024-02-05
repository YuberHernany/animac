from manim import *

class PendienteIntercepto(Scene):
    def construct(self):
        ecu_generica_por_partes = [Tex(r"$y = $"), Tex(r"$\ m \ $"), Tex(r"$\cdot x + \ $"), Tex(r"$\ b$")]
        for parte in ecu_generica_por_partes:
            parte.scale(4)
        ecu_generica = VGroup(*ecu_generica_por_partes).arrange(RIGHT)
        caja_m = SurroundingRectangle(ecu_generica_por_partes[1])
        caja_b = SurroundingRectangle(ecu_generica_por_partes[3])
        self.add_sound("m_y_b.mp3")
        self.play(Create(ecu_generica))
        self.wait(2)
        anota_m = Vector(DOWN).next_to(caja_m, DOWN).set_color(YELLOW)
        anota_b = Vector(UP).next_to(caja_b, UP).set_color(YELLOW)
        nombre_m = Text("Pendiente").scale(2).next_to(anota_m, DOWN).set_color(YELLOW)
        nombre_b = Text("Intercepto").scale(2).next_to(anota_b, UP).set_color(YELLOW).shift(LEFT)
        self.wait(2)
        for cosa in [caja_m, anota_m, nombre_m, caja_b, anota_b, nombre_b]:
            self.play(Create(cosa))
            self.wait(0.4)
        for cosa in [caja_m, anota_m, nombre_m, caja_b, anota_b, nombre_b, ecu_generica]:
            self.play(Uncreate(cosa), run_time=0.001)

        # ejemplo 1
        ecu_generica_por_partes_1 = [Tex(r"$y = $"), Tex(r"$\ 2 \ $"), Tex(r"$\cdot x + \ $"), Tex(r"$\ 3$")]
        for parte in ecu_generica_por_partes_1:
            parte.scale(4)
        ecu_generica_1 = VGroup(*ecu_generica_por_partes_1).arrange(RIGHT)
        caja_m = SurroundingRectangle(ecu_generica_por_partes_1[1])
        caja_b = SurroundingRectangle(ecu_generica_por_partes_1[3])
        self.add_sound("m_y_b.mp3")
        self.play(Create(ecu_generica_1))
        self.wait(2)
        anota_m = Vector(DOWN).next_to(caja_m, DOWN).set_color(YELLOW)
        anota_b = Vector(UP).next_to(caja_b, UP).set_color(YELLOW)
        nombre_m = Text("Pendiente").scale(2).next_to(anota_m, DOWN).set_color(YELLOW)
        nombre_b = Text("Intercepto").scale(2).next_to(anota_b, UP).set_color(YELLOW).shift(LEFT)
        self.wait(2)
        for cosa in [caja_m, anota_m, nombre_m, caja_b, anota_b, nombre_b]:
            self.play(Create(cosa))
            self.wait(0.4)
        for cosa in [caja_m, anota_m, nombre_m, caja_b, anota_b, nombre_b, ecu_generica_1]:
            self.play(Uncreate(cosa), run_time=0.001)
            
        # ejemplo 2
        ecu_generica_por_partes_2 = [Tex(r"$y = $"), Tex(r"$-\frac{3}{4} \ $"), Tex(r"$\cdot x + \ $"), Tex(r"$(-\frac{2}{5})$")]
        for parte in ecu_generica_por_partes_2:
            parte.scale(3.8)
        ecu_generica_2 = VGroup(*ecu_generica_por_partes_2).arrange(RIGHT)
        caja_m = SurroundingRectangle(ecu_generica_por_partes_2[1])
        caja_b = SurroundingRectangle(ecu_generica_por_partes_2[3])
        self.add_sound("m_y_b.mp3")
        self.play(Create(ecu_generica_2))
        self.wait(2)
        anota_m = Vector(DOWN).next_to(caja_m, DOWN).set_color(YELLOW)
        anota_b = Vector(UP).next_to(caja_b, UP).set_color(YELLOW)
        nombre_m = Text("Pendiente").scale(2).next_to(anota_m, DOWN).set_color(YELLOW)
        nombre_b = Text("Intercepto").scale(2).next_to(anota_b, UP).set_color(YELLOW).shift(LEFT)
        self.wait(2)
        for cosa in [caja_m, anota_m, nombre_m, caja_b, anota_b, nombre_b]:
            self.play(Create(cosa))
            self.wait(0.4)
        for cosa in [caja_m, anota_m, nombre_m, caja_b, anota_b, nombre_b, ecu_generica_2]:
            self.play(Uncreate(cosa), run_time=0.001)
        self.wait(1) 