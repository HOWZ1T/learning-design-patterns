from Factory.factory import ShapeFactory


shape_factory = ShapeFactory()
shape1 = shape_factory.get_shape("circle")
shape1.draw()

shape2 = shape_factory.get_shape("rectangle")
shape2.draw()

shape3 = shape_factory.get_shape("square")
shape3.draw()
