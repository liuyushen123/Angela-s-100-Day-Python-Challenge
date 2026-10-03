from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.exc import IntegrityError
from __init__ import db


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    @classmethod
    def find_cafe_by_id(cls, id):
        return db.session.get(cls, id)

    @classmethod
    def get_all_atrribute(cls):
        return cls.__table__.columns.keys()  # type: ignore

    @classmethod
    def get_random_cafe(cls):
        return (
            db.session.execute(db.select(cls).order_by(db.func.random()))
            .scalars()
            .first()
        )

    @classmethod
    def add_cafe(cls, *args):
        cafe = cls(
            name=args[0],  # type: ignore
            map_url=args[1],  # type: ignore
            img_url=args[2],  # type: ignore
            location=args[3],  # type: ignore
            seats=args[4],  # type: ignore
            has_toilet=args[5],  # type: ignore
            has_wifi=args[6],  # type: ignore
            has_sockets=args[7],  # type: ignore
            can_take_calls=args[8],  # type: ignore
            coffee_price=args[9],  # type: ignore
        )

        db.session.add(cafe)
        db.session.commit()
        return

    @classmethod
    def update_cafe(cls, cafe_id, attribute, value):
        columns = cls.__table__.columns  # type: ignore
        if attribute not in columns or columns[attribute].primary_key:
            return f"Cannot update '{attribute}'"

        cafe = db.session.get(cls, cafe_id)
        if cafe is None:
            return f"No cafe with id {cafe_id}"

        py_type = columns[attribute].type.python_type  # bool, int or str

        if py_type is bool:
            value = str(value).lower() in ("1", "true", "yes")
        else:
            try:
                value = py_type(value)  # int("5") -> 5, str("abc") -> "abc"
            except ValueError:
                return f"'{attribute}' must be of type {py_type.__name__}"

        setattr(cafe, attribute, value)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return f"Could not update cafe: {e.orig}"
        return cafe

    @classmethod
    def get_all_cafes(cls):
        return db.session.execute(db.select(cls)).scalars().all()

    @classmethod
    def get_first_cafe(cls):
        return (
            db.session.execute(db.select(cls).order_by(cls.id.asc())).scalars().first()
        )

    @classmethod
    def get_last_cafe(cls):
        return (
            db.session.execute(db.select(cls).order_by(cls.id.desc())).scalars().first()
        )

    @classmethod
    def find_cafe(cls, attribute, value):
        valid_columns = cls.__table__.columns.keys()  # type: ignore
        if attribute not in valid_columns:
            raise ValueError(
                f"Cannot search by '{attribute}'. Valid options: {valid_columns}"
            )

        return cls.query.filter_by(**{attribute: value}).all()

    @classmethod
    def delete_cafe(cls, id):

        cafe = cls.find_cafe_by_id(id)
        if cafe is None:
            raise LookupError(f"No cafe with id {id}")

        db.session.delete(cafe)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Could not delete cafe: {e}"
        return f"Cafe({id}) id now deleted"

    def to_dict(self):
        return {
            column.name: getattr(self, column.name, "None") for column in self.__table__.columns  # type: ignore
        }
