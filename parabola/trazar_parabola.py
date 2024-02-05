from manim import *

class TrazaParabola(Scene):
    def construct(self):
        tex_ppal = MathTex("f(x) =", "a", "x ^{2}", "+", 'b', 'x', '+', "c").scale(3).to_edge(UL)
        tex_spal = MathTex("f(x) =", "2", "x ^{2}", "+", '3', 'x', '+', "1").scale(3).next_to(tex_ppal, DOWN)
        colores = [YELLOW, BLUE, RED]
        for k,c in zip([1,4,7], colores):
            tex_ppal[k].set_color(c)
            tex_spal[k].set_color(c)
        self.add(tex_ppal,tex_spal)
        self.wait(1)
        cajas_up = VGroup(*[SurroundingRectangle(obj).set_color(c) for obj, c in zip([tex_ppal[k] for k in [1,4,7]], colores) ])
        cajas_dowb = VGroup(*[SurroundingRectangle(obj).set_color(c) for obj, c in zip([tex_spal[k] for k in [1,4,7]], colores) ])
        for c1, c2 in zip(cajas_up, cajas_dowb):
            self.play(Transform(c1, c2))
        self.wait(1)
        todo = Group(*[tex_ppal, tex_spal, cajas_dowb, cajas_up])
        self.play(FadeOut(todo))    
        self.wait(1)
        # otro ejemplo
        tex_ppal = MathTex("f(x) =", "a", "x ^{2}", "+b", 'x', '+', "c").scale(3).to_edge(UL)
        tex_spal = MathTex("f(x) =", "-2", "x ^{2}", "-3", 'x', '+', "1").scale(3).next_to(tex_ppal, DOWN)
        colores = [YELLOW, BLUE, RED]
        for k,c in zip([1,3,6], colores):
            tex_ppal[k].set_color(c)
            tex_spal[k].set_color(c)
        self.add(tex_ppal,tex_spal)
        self.wait(1)
        cajas_up = VGroup(*[SurroundingRectangle(obj).set_color(c) for obj, c in zip([tex_ppal[k] for k in [1,3,6]], colores) ])
        cajas_dowb = VGroup(*[SurroundingRectangle(obj).set_color(c) for obj, c in zip([tex_spal[k] for k in [1,3,6]], colores) ])
        for c1, c2 in zip(cajas_up, cajas_dowb):
            self.play(Transform(c1, c2))
        self.wait(1)
        todo = Group(*[tex_ppal, tex_spal, cajas_dowb, cajas_up])
        self.play(FadeOut(todo))    
        self.wait(1)

        mensaje =  Text("Pasos para graficar parábola").to_edge(UP)
        texto1 = Text("1. Construya el número:   ").next_to(mensaje, DOWN)
        texto2 = Text("2. Grafique el vértice:   ").next_to(texto1, DOWN)
        texto3 = Text("3. Grafique el intercepto:   ").next_to(texto2, DOWN)
        self.play(Write(mensaje))
        medio = MathTex("m = \\frac{-b}{2a}").next_to(texto1, RIGHT)
        self.play(Write(texto1))
        self.play(Write(medio))
        self.play(Write(texto2))
        coords = MathTex("(m, f(m))").next_to(medio, DOWN)
        self.play(Write(coords))
        inter = MathTex("(0, c)").next_to(coords, DOWN)
        self.play(Write(texto3))
        self.play(Write(inter))
        texto4 = Text("4. Curva desde el vértice al intercepto").next_to(texto3, DOWN)
        self.play(Write(texto4))
        texto5 = Text("5. Complete con simetría").next_to(texto4, DOWN)
        self.play(Write(texto5))
        self.wait(1)