from Factory import shape


class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type is None:
            return None

        shape_type = shape_type.lower()

        if shape_type == "circle":
            return shape.Circle()
        elif shape_type == "rectangle":
            return shape.Rectangle()
        elif shape_type == "square":
            return shape.Square()

        return None
