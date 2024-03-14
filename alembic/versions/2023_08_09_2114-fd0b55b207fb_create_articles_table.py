"""Create articles table.

Revision ID: fd0b55b207fb
Revises:
Create Date: 2023-08-09 21:14:29.733520
"""
import uuid

import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext.asyncio import AsyncAttrs

from alembic import op


# revision identifiers, used by Alembic.
revision = "fd0b55b207fb"
down_revision = None
branch_labels = None
depends_on = None


class Base(AsyncAttrs, sqlalchemy.orm.DeclarativeBase):
    pass


class Article(Base):
    __tablename__ = "articles"

    article_id: sqlalchemy.orm.Mapped[uuid.UUID] = sqlalchemy.orm.mapped_column(primary_key=True)
    title: sqlalchemy.orm.Mapped[str]
    preview: sqlalchemy.orm.Mapped[str]
    body: sqlalchemy.orm.Mapped[str]
    created_by: sqlalchemy.orm.Mapped[int]


def upgrade() -> None:
    database_engine = op.get_bind()
    Base.metadata.create_all(database_engine)

    session: sqlalchemy.orm.Session = sqlalchemy.orm.Session(bind=database_engine)

    session.execute(
        sqlalchemy.insert(Article),
        [
            {
                "article_id": uuid.uuid4(),
                "title": "Влияние социальных сетей на молодежь: плюсы и минусы",
                "preview": "Статья исследует влияние активного присутствия в социальных сетях "
                "на подростков и молодых людей, раскрывая как положительные, "
                "так и отрицательные аспекты этого воздействия.",
                "body": "В эпоху цифровой коммуникации социальные сети стали неотъемлемой частью "
                "жизни молодежи. Положительными аспектами использования социальных "
                "платформ являются расширение круга общения, возможность самовыражения "
                "и доступ к информации. Однако, увлечение социальными сетями может "
                "привести к снижению реальных социальных контактов, а также вызвать "
                "проблемы с психическим здоровьем из-за стресса, сравнения с другими "
                "и негативных воздействий контента.",
                "created_by": 1,
            },
            {
                "article_id": uuid.uuid4(),
                "title": "Зеленые технологии: будущее экологически ответственной энергетики",
                "preview": "В этой статье исследуется важность развития и внедрения зеленых "
                "технологий для устойчивого будущего энергетики, а также их позитивное "
                "воздействие на окружающую среду.",
                "body": "В условиях изменения климата и исчерпания традиционных источников "
                "энергии, зеленые технологии становятся ключевым элементом экологически "
                "ответственного развития. Солнечные и ветровые электростанции, "
                "геотермальные системы и биоэнергетика — все эти инновации не только "
                "снижают выбросы парниковых газов, но и способствуют созданию новых "
                "рабочих мест и экономическому росту.",
                "created_by": 1,
            },
            {
                "article_id": uuid.uuid4(),
                "title": "Искусство медитации: путь к гармонии души и тела",
                "preview": "Статья рассматривает пользу и эффекты медитации на физическое и "
                "психическое здоровье человека, а также предоставляет практические "
                "советы для начинающих.",
                "body": "Медитация, практикуемая веками, обретает новое значение в современном "
                "мире. Научные исследования подтверждают, что регулярная медитативная "
                "практика способствует снижению уровня стресса, улучшению концентрации, "
                "а также нормализации кровяного давления. Она помогает находить "
                "внутренний покой в суете повседневной жизни и находить гармонию между "
                "душой и телом.",
                "created_by": 2,
            },
            {
                "article_id": uuid.uuid4(),
                "title": "Искусство кулинарии: от рецепта к творчеству",
                "preview": "В этой статье рассматривается кулинария как форма искусства, "
                "способствующая не только приготовлению вкусных блюд, "
                "но и самовыражению через творчество на кухне.",
                "body": "Готовить еду — это гораздо больше, чем просто пополнить желудок. "
                "Это искусство, которое позволяет объединить вкусы, ароматы и текстуры "
                "в гармоничное произведение. Кулинария стала платформой для экспериментов "
                "с ингредиентами, создания новых блюд и выражения креативности. "
                "Современные шеф-повары не только следуют рецептам, но и добавляют в них "
                "частичку себя, превращая обед в настоящее искусство.",
                "created_by": 2,
            },
            {
                "article_id": uuid.uuid4(),
                "title": "Изучение иностранных языков: расширение кognitivных горизонтов",
                "preview": "Статья анализирует преимущества изучения иностранных языков, включая "
                "их позитивное влияние на когнитивные функции мозга и расширение "
                "культурного понимания.",
                "body": "Способность говорить на нескольких языках открывает двери к новым мирам. "
                "Помимо очевидных коммуникативных выгод, изучение иностранных языков "
                "имеет положительный эффект на мозговую активность. Это улучшает "
                "способность к аналитическому мышлению, повышает креативность и укрепляет "
                "память. Кроме того, овладение языком позволяет более глубоко понять "
                "культуру, обычаи и ценности других народов, способствуя толерантности "
                "и межкультурному диалогу.",
                "created_by": 3,
            },
        ],
    )


def downgrade() -> None:
    database_engine = op.get_bind()
    Base.metadata.drop_all(database_engine)
