from Abstract_Factory.factories import FactoryProducer


# demo shape factory
shape_factory = FactoryProducer.get_factory("shape")

shape1 = shape_factory.get_shape("circle")
shape1.draw()

shape2 = shape_factory.get_shape("rectangle")
shape2.draw()

shape3 = shape_factory.get_shape("square")
shape3.draw()


# demo color factory
color_factory = FactoryProducer.get_factory("color")

color1 = color_factory.get_color("red")
color1.fill()

color2 = color_factory.get_color("green")
color2.fill()

color3 = color_factory.get_color("blue")
color3.fill()
