from manim import *

class Recta(Scene):
    def construct(self):
        plane = NumberPlane().set_opacity(0.5)
        tex_pendiente_intercepto = Tex(r"$y = m x + b, $").scale(2).shift(3*UP + 4*LEFT)
        self.add(plane, tex_pendiente_intercepto)
        pendiente = DecimalNumber(0.3, num_decimal_places=1).scale(2).shift(3*UP + 2*RIGHT)
        intercepto = DecimalNumber(0, num_decimal_places=1).scale(2).shift(3*UP + 6*RIGHT)
        tex_m = Tex(r"$m = $")
        tex_b = Tex(r"$b = $")
        text_coma = Text(",").scale(2).next_to(pendiente).shift(0.5*DOWN)
        tex_m.scale(2).next_to(pendiente, LEFT)
        tex_b.scale(2).next_to(intercepto, LEFT)
        self.add(tex_m, tex_b, text_coma)
        self.add(pendiente, intercepto)
        tracker_m = ValueTracker(0.3)
        tracker_b = ValueTracker(0)
        pendiente.add_updater(lambda d: d.set_value(tracker_m.get_value()))
        intercepto.add_updater(lambda d: d.set_value(tracker_b.get_value()))
        # self.play(tracker_m.animate.set_value(2))
        self.wait(2)
        
        # primera etapa x's

        number_line_x = NumberLine().add_numbers()
        pointer_x = Dot(ORIGIN)
        label_x = MathTex("x").add_updater(lambda m: m.next_to(pointer_x, UP))

        tracker = ValueTracker(0)
        pointer_x.add_updater(
            lambda m: m.next_to(
                        number_line_x.n2p(tracker.get_value())
                    )
        )
        self.add(number_line_x, pointer_x,label_x)
        tracker += 2
        self.wait(1)
        tracker -= 6
        self.wait(0.5)
        self.play(tracker.animate.set_value(6)),
        self.wait(0.5)
        self.play(tracker.animate.set_value(2))
        self.play(tracker.animate.increment_value(-4))
        self.wait(0.5)
        self.remove(pointer_x, label_x)

        # respecto a y

        number_line_y = NumberLine().rotate(90*DEGREES).add_numbers()
        pointer_y = Dot(ORIGIN)
        label_y = MathTex("y").add_updater(lambda m: m.next_to(pointer_y, RIGHT))

        tracker = ValueTracker(0)
        pointer_y.add_updater(
            lambda m: m.move_to(
                        number_line_y.n2p(tracker.get_value())
                    )
        )
        self.add(number_line_y, pointer_y,label_y)
        tracker += 1
        self.wait(1)
        tracker -= 3
        self.wait(0.5)
        self.play(tracker.animate.set_value(3)),
        self.wait(0.5)
        self.play(tracker.animate.set_value(1))
        self.play(tracker.animate.increment_value(-2))
        self.wait(0.5)
        self.remove(pointer_y, label_y)

        def funcion_lineal(pendiente, intercepto, x):
            return pendiente * x + intercepto
        

class PendienteIntercepto(Scene):
    def construct(self):
        def lineal(x):
            return 2*x + 1
        # reemplaza valores para tabla
        self.wait(3)
        self.add_sound('sp1_r.mp3')
        tabla1 = MathTable(
        [[-1,""], [1, ""]],
        col_labels=[MathTex("x"), MathTex("y")],
        include_outer_lines=True).to_edge(UR).set_color(YELLOW)
        self.add(tabla1)
        self.wait(1)

        eq1 = MathTex("y", "=", "m", "x", "+", "b").scale(2).to_edge(UL).set_color(YELLOW)
        eq2 = MathTex("y", "=", "2", "x", "+", "1").scale(2).set_color(YELLOW).next_to(eq1, DOWN)
        eq2a = MathTex("y", "=", "2", "(-1)", "+", "1").scale(2).set_color(YELLOW).next_to(eq2, DOWN)
        eq2b = MathTex("y", "=", "-2", "+", "1").scale(2).set_color(YELLOW).next_to(eq2a, DOWN)
        eq2c = MathTex("y", "=", "-1").scale(2).set_color(YELLOW).next_to(eq2b, DOWN)
        eval1 = MathTex("y", "=", "2", "(-1)", "+", "1").scale(2).set_color(YELLOW).next_to(eq2, DOWN)
        eval2 = MathTex("y", "=", "2", "(1)", "+", "1").scale(2).set_color(YELLOW).next_to(eq2, DOWN)

        # aparece plano
        plano = NumberPlane().set_opacity(0.7)
        # eje_x = NumberLine().add_numbers()

        # introduce pendiente intercepto
        # self.play(Write(eq1))
        self.add_sound('sp2_r.mp3')
        self.add(plano, eq1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.play(FadeIn(eq2a))
        self.play(FadeIn(eq2b))
        self.play(FadeIn(eq2c))
        self.wait(1)

        res1 = MathTex("-1").scale(2)
        res2 = MathTex("3").scale(2)
        res1.next_to(eq2c, RIGHT)
        self.play(res1.animate.shift(RIGHT*7.5+UP*3.5))
        self.wait(1)
        self.play(FadeOut(eq2), FadeOut(eq2a), FadeOut(eq2b), FadeOut(eq2c))
        self.wait(1)

        eq1 = MathTex("y", "=", "m", "x", "+", "b").scale(2).to_edge(UL).set_color(YELLOW)
        eq2 = MathTex("y", "=", "2", "x", "+", "1").scale(2).set_color(YELLOW).next_to(eq1, DOWN)
        eq2a = MathTex("y", "=", "2", "(1)", "+", "1").scale(2).set_color(YELLOW).next_to(eq2, DOWN)
        eq2b = MathTex("y", "=", "2", "+", "1").scale(2).set_color(YELLOW).next_to(eq2a, DOWN)
        eq2c = MathTex("y", "=", "3").scale(2).set_color(YELLOW).next_to(eq2b, DOWN)
        self.add_sound('sp2_r.mp3')
        self.play(TransformMatchingTex(eq1, eq2))
        self.play(FadeIn(eq2a))
        self.play(FadeIn(eq2b))
        self.play(FadeIn(eq2c))
        self.wait(1)
        res2.next_to(eq2c, RIGHT)
        self.play(res2.animate.shift(RIGHT*8.5+UP*2.2))
        self.wait(1)
        self.play(FadeOut(eq2), FadeOut(eq2a), FadeOut(eq2b), FadeOut(eq2c))
        self.wait(1)

        #poner numeracion a los ejes
        eje_x = NumberLine().add_numbers()
        eje_y = NumberLine().add_numbers().rotate(90*DEGREES).shift(0.3*RIGHT+0.1*UP)
        self.add(eje_x, eje_y)
        self.wait(1)

        # graficar recta
        self.add_sound('sp3_r.mp3')
        p1 = Dot([0,0,0]).scale(2).set_color(YELLOW)
        self.play(p1.animate.shift(LEFT))
        self.wait(1)
        self.play(p1.animate.shift(DOWN))
        self.wait(5)
        p2 = Dot([0,0,0]).scale(2).set_color(YELLOW)
        self.play(p2.animate.shift(RIGHT))
        self.wait(1)
        self.play(p2.animate.shift(3*UP))
        self.wait(1)
        l1 = Line(3*LEFT+5*DOWN, 2*RIGHT+5*UP).set_color(RED)
        self.play(Create(l1))
        self.wait(1)
 


class PruebaDeNumeracionDeEjes(Scene):
    def construct(self):
        plano = NumberPlane()
        eje_x = NumberLine().add_numbers()
        eje_y = NumberLine().add_numbers().rotate(90*DEGREES).shift(0.3*RIGHT+0.1*UP)
        self.add(plano, eje_x, eje_y)
        self.wait(1)


class PuntosEnElPlanoCartesiano(Scene):
    def construct(self):
        plano = NumberPlane()
        self.add_sound("ubicar_puntos_en_el_plano.mp3")
        self.play(Create(plano), run_time=5)
        ubicaciones = [(3,2), (4,1), (-2,-2), (-3,2), (-4, -3), (5,0), (0,-3)]
        colores = [RED, BLUE, YELLOW, PINK, ORANGE, GREEN, PURPLE]
        coords = [MathTex(str(ubi)).scale(2).to_edge(UL).set_color(c) for ubi, c in zip(ubicaciones, colores)]
        puntos = [Dot(ORIGIN).scale(2).set_color(c) for _, c in zip(range(7), colores)]
        for cor, pun, ubi in zip(coords, puntos, ubicaciones):
            self.play(Write(cor))
            self.play(pun.animate.shift(ubi[0]*RIGHT))
            self.play(pun.animate.shift(ubi[1]*UP))
            cor.scale(0.5)
            self.play(cor.animate.next_to(pun, DOWN))
        self.wait(1)
