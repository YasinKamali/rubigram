from typing import TypeVar
from dataclasses import fields


T = TypeVar("T")


class Base:
    def __repr__(self) -> str:

        class_name = self.__class__.__name__

        instance_fields = fields(self)

        fields_repr_list = []

        for field_info in instance_fields:
            field_name = field_info.name
            field_value = getattr(self, field_name)

            if field_name == "raw" or field_info.metadata.get("repr", True) is False:
                continue

            try:
                field_repr = repr(field_value)
            except Exception:
                field_repr = f"<{type(field_value).__name__} object>"

            fields_repr_list.append(f"{field_name}={field_repr}")

        formatted_fields = "\n    ".join(fields_repr_list)

        return f"{class_name}(\n    {formatted_fields}\n)"