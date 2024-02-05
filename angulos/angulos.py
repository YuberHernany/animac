from manim import *
import numpy as np 

class AngulosRectos(Scene):
    def construct(self):
        # para definir agudo, recto, opuesto por vertice y obtuso
        t_rectos = Text('ángulos rectos').to_edge(UL)
        self.play(Write(t_rectos))
        self.add_sound('cuatro_angs_rectos.mp3')
        l1 = Line(start=4*LEFT, end=4*RIGHT, stroke_width=10).set_color(ORANGE)
        l2 = Line(start=4*DOWN, end=4*UP, stroke_width=10).set_color(ORANGE)
        alpha = Angle(l1, l2, quadrant=(1,1), stroke_width=10, radius=2)
        alpha1 = alpha.copy()
        alpha2 = alpha.copy().rotate(angle=PI/2, about_point=ORIGIN)
        alpha3 = alpha.copy().rotate(angle=PI, about_point=ORIGIN)
        alpha4 = alpha.copy().rotate(angle=3*PI/2, about_point=ORIGIN)
        alphas = VGroup(*[alpha1, alpha2, alpha3, alpha4])
        self.add(l1, l2)
        self.wait(3)

        # valores
        t = MathTex("90^{\circ}").scale(2) 
        t1 = t.copy().shift(0.8*RIGHT+0.8*UP)
        t2 = t.copy().shift(0.8*LEFT+0.8*UP)
        t3 = t.copy().shift(0.8*LEFT+0.8*DOWN)
        t4 = t.copy().shift(0.8*RIGHT+0.8*DOWN)
        textos = VGroup(*[t1,t2,t3,t4])
        for ang, text in zip(alphas, textos):
            self.play(Create(ang), Write(text))
            self.play(FadeOut(ang), FadeOut(text))
        self.play(FadeOut(t_rectos))
        self.play(FadeOut(l1), FadeOut(l2))
        self.wait(2)

        # ahora angulos agudos y obtusos

class AgudoObtuso(Scene):
    def construct(self):
        self.add_sound('agudos_y_obtusos.mp3')
        l1 = Line(start=4*LEFT, end=4*RIGHT, stroke_width=10).set_color(ORANGE)
        l2 = Line(start=4*DOWN+4*LEFT, end=4*UP+4*RIGHT, stroke_width=10).set_color(ORANGE)
        alpha45 = Angle(l1, l2, quadrant=(1,1), stroke_width=10, radius=2)
        arc135 = Arc(radius=2, start_angle=0, angle=135*DEGREES, stroke_width=10).rotate(45*DEGREES, about_point=ORIGIN)

        self.add(l1, l2)
        self.wait(3)

        # valores
        t45 = MathTex("45^{\circ}").scale(2).shift(1.2*RIGHT+0.4*UP)
        t135 = MathTex("135^{\circ}").scale(2).shift(0.5*LEFT+0.8*UP)
        textos = VGroup(*[t45, t135])
        mensajes = [Text('ángulo agudo').to_edge(UR), Text('ángulo obtuso').to_edge(UL)]
        for ang, text, men in zip([alpha45, arc135], textos, mensajes):
            self.play(Create(ang), Write(text), Write(men), run_time=5)
            self.play(FadeOut(ang), FadeOut(text), FadeOut(men), run_time=5)
        self.wait(2)


class Complementarios(Scene):
    def construct(self):
        titulo = Text("ángulos complementarios").set_color(BLUE).to_edge(DL)
        self.play(Write(titulo))
        self.add_sound('angulos_complementarios.mp3')
        l1 = Line(start=ORIGIN, end=4*RIGHT, stroke_width=10).set_color(ORANGE)
        l2 = Line(start=ORIGIN, end=4*RIGHT+1.3*np.sqrt(3)*UP, stroke_width=10).set_color(ORANGE)
        l3 = Line(start=ORIGIN, end=4*UP, stroke_width=10).set_color(ORANGE)
        arc30 = Arc(radius=2, angle=30*DEGREES, stroke_width=10).set_color(PINK)
        arc60 = Arc(radius=2, angle=60*DEGREES, stroke_width=10).rotate(30*DEGREES, about_point=ORIGIN)
        self.add(l1, l2, l3)
        self.wait(1)
        t30 = MathTex("30^{\circ}").scale(1.5).shift(1.2*RIGHT+0.4*UP).set_color(PINK)
        T30 = t30.copy().to_edge(UL)
        mas = MathTex("+").scale(1.5).next_to(T30)
        t60 = MathTex("60^{\circ}").scale(1.5).shift(0.5*RIGHT+1.2*UP)
        T60 = t60.copy().next_to(mas, RIGHT)
        T90 = MathTex(" = 90^{\circ}").scale(1.5).next_to(T60, RIGHT)

        textos = VGroup(*[t30, t60])
        for a, t in zip([arc30, arc60], textos):
            self.play(Create(a), Write(t))
        self.wait(2)
        self.play(Write(T30))
        self.play(Write(mas))
        self.play(Write(T60))
        self.play(Write(T90))
        self.play(Circumscribe(T90), run_time=3)
        self.wait(2)

class Suplementarios(Scene):
    def construct(self):
        titulo = Text("ángulos suplementarios").set_color(BLUE).to_edge(DL)
        self.play(Write(titulo))
        self.add_sound('angulos_suplementarios.mp3')
        l1 = Line(start=ORIGIN, end=4*RIGHT, stroke_width=10).set_color(ORANGE)
        l2 = Line(start=ORIGIN, end=4*RIGHT+1.3*np.sqrt(3)*UP, stroke_width=10).set_color(ORANGE)
        l3 = Line(start=ORIGIN, end=4*LEFT, stroke_width=10).set_color(ORANGE)
        arc30 = Arc(radius=2, angle=30*DEGREES, stroke_width=10).set_color(PINK)
        arc150 = Arc(radius=2, angle=150*DEGREES, stroke_width=10).rotate(30*DEGREES, about_point=ORIGIN)
        self.add(l1, l2, l3)
        self.wait(1)
        t30 = MathTex("30^{\circ}").scale(1.5).shift(1.2*RIGHT+0.4*UP).set_color(PINK)
        T30 = t30.copy().to_edge(UL)
        mas = MathTex("+").scale(1.5).next_to(T30)
        t150 = MathTex("150^{\circ}").scale(1.5).shift(0.5*LEFT+1.2*UP)
        T150 = t150.copy().next_to(mas, RIGHT)
        T180 = MathTex(" = 180^{\circ}").scale(1.5).next_to(T150, RIGHT)
        textos = VGroup(*[t30, t150])
        for a, t in zip([arc30, arc150], textos):
            self.play(Create(a), Write(t))
        self.wait(2)

    
        self.play(Write(T30))
        self.play(Write(mas))
        self.play(Write(T150))
        self.play(Write(T180))
        self.play(Circumscribe(T180), run_time=3)
        self.wait(2)

class Cuerda(Scene):
    def construct(self):
        cir = Circle(radius=3, stroke_width=10).set_color(ORANGE)
        centro = Dot(ORIGIN)
        self.play(Create(centro), Create(cir))
        self.wait(2)
        coords18 = 3*np.array([[np.cos(2*k*PI/18), np.sin(2*k*PI/18), 0] for k in range(18)])
        cuerda_chica = Line(coords18[6], coords18[4], stroke_width=10).set_color(GREEN)
        cuerda_mediana = Line(coords18[7], coords18[2], stroke_width=10).set_color(GREEN)
        cuerda_grande = Line(coords18[8], coords18[0], stroke_width=10).set_color(GREEN)
        diametro = Line(coords18[9], coords18[0], stroke_width=10)
        t_cuerda = Text("Cuerda").to_edge(UL)
        t_diametro = Text('Diámetro').shift(0.7*DOWN)
        self.play(Create(cuerda_chica), Write(t_cuerda))
        self.wait(1)
        self.play(Transform(cuerda_chica, cuerda_mediana), run_time=3)
        self.play(Transform(cuerda_chica, cuerda_grande), run_time=3)
        self.play(Transform(cuerda_chica, diametro), Transform(t_cuerda, t_diametro), run_time=3)
        # self.add(centro, cir, cuerda_chica, cuerda_mediana, cuerda_grande, diametro)
        self.wait(1)

class QueEsPI(Scene):
    def construct(self):
        cir = Circle(radius=2, stroke_width=10).set_color(ORANGE)
        peri_lineal = Line(2*PI*LEFT, 2*PI*RIGHT, stroke_width=10).to_edge(UL).set_color(ORANGE)
        diametro = Line(2*LEFT, 2*RIGHT, stroke_width=10)
        diametro_lineal = Line(2*LEFT, 2*RIGHT, stroke_width=10).next_to(peri_lineal, DOWN).shift(DOWN)
        self.play(Create(cir))
        self.play(Create(diametro))
        self.wait(2)
        self.play(Transform(cir, peri_lineal), run_time=3)
        self.play(Transform(diametro, diametro_lineal), run_time=2)
        self.wait(1)
        tx_cir = MathTex("6.2832\\ cm").next_to(peri_lineal, DOWN).set_color(ORANGE)
        sym_div = MathTex("/")
        tx_dia = MathTex("2.0\\ cm").next_to(diametro_lineal, DOWN)
        self.play(Write(tx_cir))
        self.play(Write(tx_dia))
        self.wait(2)
        self.play(tx_cir.animate.to_edge(DL))
        self.play(sym_div.animate.next_to(tx_cir, RIGHT))
        self.play(tx_dia.animate.next_to(sym_div, RIGHT))
        resul = MathTex("= 3.1416 = \pi").scale(1.5).set_color(YELLOW).next_to(tx_dia, RIGHT)
        self.play(Write(resul))
        self.wait(2)
        todo = [cir, peri_lineal, diametro, diametro_lineal, tx_cir, sym_div, tx_dia, resul]
        for cosa in todo:
            self.play(FadeOut(cosa), run_time=0.001)
        self.wait(1)

        cir = Circle(radius=1, stroke_width=10).set_color(ORANGE)
        peri_lineal = Line(1*PI*LEFT, 1*PI*RIGHT, stroke_width=10).to_edge(UL).set_color(ORANGE)
        diametro = Line(1*LEFT, 1*RIGHT, stroke_width=10)
        diametro_lineal = Line(1*LEFT, 1*RIGHT, stroke_width=10).next_to(peri_lineal, DOWN).shift(DOWN)
        self.play(Create(cir))
        self.play(Create(diametro))
        self.wait(2)
        self.play(Transform(cir, peri_lineal), run_time=3)
        self.play(Transform(diametro, diametro_lineal), run_time=2)
        self.wait(1)
        tx_cir = MathTex("3.1416\\ cm").next_to(peri_lineal, DOWN).set_color(ORANGE)
        sym_div = MathTex("/")
        tx_dia = MathTex("1.0\\ cm").next_to(diametro_lineal, DOWN)
        self.play(Write(tx_cir))
        self.play(Write(tx_dia))
        self.wait(2)
        self.play(tx_cir.animate.to_edge(DL))
        self.play(sym_div.animate.next_to(tx_cir, RIGHT))
        self.play(tx_dia.animate.next_to(sym_div, RIGHT))
        resul = MathTex("= 3.1416 = \pi").scale(1.5).set_color(YELLOW).next_to(tx_dia, RIGHT)
        self.play(Write(resul))
        self.wait(2)
        todo = [cir, peri_lineal, diametro, diametro_lineal, tx_cir, sym_div, tx_dia, resul]
        for cosa in todo:
            self.play(FadeOut(cosa), run_time=0.001)
        self.wait(1)

        cir = Circle(radius=0.5, stroke_width=10).set_color(ORANGE)
        peri_lineal = Line(0.5*PI*LEFT, 0.5*PI*RIGHT, stroke_width=10).to_edge(UL).set_color(ORANGE)
        diametro = Line(0.5*LEFT, 0.5*RIGHT, stroke_width=10)
        diametro_lineal = Line(0.5*LEFT, 0.5*RIGHT, stroke_width=10).next_to(peri_lineal, DOWN).shift(DOWN)
        self.play(Create(cir))
        self.play(Create(diametro))
        self.wait(2)
        self.play(Transform(cir, peri_lineal), run_time=3)
        self.play(Transform(diametro, diametro_lineal), run_time=2)
        self.wait(1)
        tx_cir = MathTex("1.57078\\ cm").next_to(peri_lineal, DOWN).set_color(ORANGE)
        sym_div = MathTex("/")
        tx_dia = MathTex("0.5\\ cm").next_to(diametro_lineal, DOWN)
        self.play(Write(tx_cir))
        self.play(Write(tx_dia))
        self.wait(2)
        self.play(tx_cir.animate.to_edge(DL))
        self.play(sym_div.animate.next_to(tx_cir, RIGHT))
        self.play(tx_dia.animate.next_to(sym_div, RIGHT))
        resul = MathTex("= 3.1416 = \pi").scale(1.5).set_color(YELLOW).next_to(tx_dia, RIGHT)
        self.play(Write(resul))
        self.wait(2)
        todo = [cir, peri_lineal, diametro, diametro_lineal, tx_cir, sym_div, tx_dia, resul]
        for cosa in todo:
            self.play(FadeOut(cosa), run_time=0.001)
        self.wait(1)

        cir = Circle(radius=2, stroke_width=10).set_color(ORANGE)
        diametro = Line(2*LEFT, 2*RIGHT, stroke_width=10)
        cir2 = Circle(radius=1, stroke_width=10).set_color(ORANGE).shift(5*LEFT)
        diametro2 = Line(LEFT, RIGHT, stroke_width=10).shift(5*LEFT)
        cir3 = Circle(radius=0.5, stroke_width=10).set_color(ORANGE).shift(5*RIGHT)
        diametro3 = Line(0.5*LEFT, 0.5*RIGHT, stroke_width=10).shift(5*RIGHT)
        self.play(FadeIn(cir, diametro))
        self.play(FadeIn(cir2, diametro2))
        self.play(FadeIn(cir3, diametro3))
        self.wait(2)
        coci1 = MathTex("\\frac{C}{D}=\pi").scale(1.5).next_to(cir, DOWN)
        coci2 = MathTex("\\frac{C}{D}=\pi").scale(1.5).next_to(cir2, DOWN)
        coci3 = MathTex("\\frac{C}{D}=\pi").scale(1.5).next_to(cir3, DOWN)
        self.play(Write(coci1))
        self.play(Write(coci2))
        self.play(Write(coci3))
        self.wait(2)
        coci_new1 = MathTex("\\frac{C}{2r}=\pi").scale(1.5).next_to(cir, DOWN)
        coci_new2 = MathTex("\\frac{C}{2r}=\pi").scale(1.5).next_to(cir2, DOWN)
        coci_new3 = MathTex("\\frac{C}{2r}=\pi").scale(1.5).next_to(cir3, DOWN)
        self.play(Transform(coci1, coci_new1))
        self.play(Transform(coci2, coci_new2))
        self.play(Transform(coci3, coci_new3))
        self.wait(2)
        coci_renew1 = MathTex("C = 2\pi r").scale(1.5).next_to(cir, DOWN)
        coci_renew2 = MathTex("C = 2\pi r").scale(1.5).next_to(cir2, DOWN)
        coci_renew3 = MathTex("C = 2\pi r").scale(1.5).next_to(cir3, DOWN)
        self.play(Transform(coci1, coci_renew1))
        self.play(Transform(coci2, coci_renew2))
        self.play(Transform(coci3, coci_renew3))
        self.wait(2)

class AreaCirculo(Scene):
    def construct(self):
        colors = [YELLOW, BLUE, RED, GREEN, ORANGE, PURPLE, DARK_BROWN, GRAY]
        cir = Circle(radius=2, stroke_width=10).set_color(ORANGE).shift(4.5*RIGHT)
        arcos = [Arc(radius=k*0.1, angle=2*PI, stroke_width=10).set_color(colors[k % 8]).shift(4.5*RIGHT) for k in range(1, 21)]
        self.add(cir)
        for a in arcos:
            self.add(a)
        self.wait(1)
        lineas = [Line((k/10)*LEFT*PI, (k/10)*RIGHT*PI, stroke_width=10).set_color(colors[k % 8]).shift(0.5*LEFT+DOWN) for k in range(1,21)]
        for l1, l2 in zip(lineas, lineas[1:]):
            l2.next_to(l1, DOWN, buff=0.1)
        for arco, l in zip(arcos, lineas):
            self.play(Transform(arco, l), run_time=0.6)
        self.wait(1)
        radio_altura = Line(ORIGIN, 2*UP, stroke_width=10).shift(4.5*RIGHT+1.95*DOWN)
        self.play(FadeIn(radio_altura), run_time=2)
        self.play(radio_altura.animate.shift(DOWN))
        self.play(radio_altura.animate.shift(1.6*PI*LEFT))
        self.wait(1)

        brace_base = Brace(lineas[-1], DOWN, buff=0)
        self.play(Create(brace_base))
        t_base = MathTex("2\pi r").next_to(brace_base, DOWN, buff=0)
        self.play(Write(t_base))
        self.play(radio_altura.animate.shift(6.2*LEFT))
        t_radio = MathTex('r').next_to(radio_altura, RIGHT)
        self.play(Write(t_radio))
        self.wait(2)
        t_area = Text("área =   ").shift(2*LEFT+2*UP)
        self.play(Write(t_area))
        sym_prod = MathTex("\\cdot")
        self.play(t_base.animate.next_to(t_area, RIGHT))
        self.play(t_base.animate.shift(0.4*RIGHT))
        self.play(t_base.animate.scale(2))
        self.play(sym_prod.animate.next_to(t_base, RIGHT))
        self.play(t_radio.animate.next_to(sym_prod, RIGHT))
        self.play(t_radio.animate.scale(2))
        dividido_dos = MathTex("/ 2").scale(2).next_to(t_radio, RIGHT)
        self.play(Write(dividido_dos))
        self.wait(3)
        self.play(FadeOut(t_base), FadeOut(sym_prod), FadeOut(t_radio), FadeOut(dividido_dos))
        resultado_area = MathTex("\pi r^2").scale(2).next_to(t_area)
        self.play(resultado_area.animate.shift(0.4*RIGHT))
        self.play(Write(resultado_area))
        resaltar = SurroundingRectangle(resultado_area, stroke_width=10)
        self.play(Create(resaltar))
        self.wait(2)
        

