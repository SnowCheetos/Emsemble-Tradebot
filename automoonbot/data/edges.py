import torch
from functools import lru_cache
from typing import Hashable, Set

from automoonbot.utils import Tense, Aspect
from automoonbot.data import Element, nodes as n


class Edges(type):
    subclasses = set()

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        if bases != (Element,):
            cls.subclasses.add(new_class)
        return new_class

    @classmethod
    def get(cls) -> Set[Element]:
        return cls.subclasses


class Edge(Element, metaclass=Edges):
    tense: Tense = None
    aspect: Aspect = None
    source_type: n.Node = None
    target_type: n.Node = None
    tensor_dim: int = None

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        mutable: bool = True,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            mutable=mutable,
            on_error=on_error,
            **kwargs,
        )

        self.source = source
        self.target = target

    def __init_subclass__(cls, *args, **kwargs) -> None:
        super().__init_subclass__(*args, **kwargs)
        cls.name = cls.__name__.lower()

    @property
    @lru_cache(maxsize=None)
    def tense(self) -> Tense:
        return self.__class__.tense

    @property
    @lru_cache(maxsize=None)
    def aspect(self) -> Aspect:
        return self.__class__.aspect

    @property
    @lru_cache(maxsize=None)
    def source_type(self) -> n.Node:
        return self.__class__.source_type

    @property
    @lru_cache(maxsize=None)
    def target_type(self) -> n.Node:
        return self.__class__.target_type

    @property
    @lru_cache(maxsize=None)
    def tensor_dim(self) -> int:
        return self.__class__.tensor_dim


class Issues(Edge):
    """
    e.g. Company A issues stock A
    """

    tense = Tense.Present
    aspect = Aspect.Simple
    source_type = n.Company
    target_type = n.Equity
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=False,
            on_error=on_error,
            **kwargs,
        )

    # TODO This ugly mess made me realized I wasn't crazy over the need for a custom script
    def get_attr(self):
        if not (self.src_element or self.tgt_element):
            return None
        elif not (self.src_element.symbol or self.tgt_element.symbol):
            return None
        elif self.src_element.symbol != self.tgt_element.symbol:
            return None
        else:
            return {0: 1}

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)


class Drafted(Edge):
    """
    e.g. Author drafted news at 4pm on June 16th
    """

    tense = Tense.Past
    aspect = Aspect.Simple
    source_type = n.Author
    target_type = n.News
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=False,
            on_error=on_error,
            **kwargs,
        )

    def get_attr(self):
        pass

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)


class Published(Edge):
    """
    e.g. Publisher published news at 9:45am
    """

    tense = Tense.Past
    aspect = Aspect.Simple
    source_type = n.Publisher
    target_type = n.News
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=False,
            on_error=on_error,
            **kwargs,
        )

    def get_attr(self):
        pass

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)


class Serves(Edge):
    """
    e.g. Author have been working at publisher since 2012
    """

    tense = Tense.Present
    aspect = Aspect.Perfect
    source_type = n.Author
    target_type = n.Publisher
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=True,
            on_error=on_error,
            **kwargs,
        )

    def get_attr(self):
        pass

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)

    def get_update(self):
        pass


class Employs(Edge):
    """
    e.g. Publisher pays author $80,000 per year
    """

    tense = Tense.Past
    aspect = Aspect.Simple
    source_type = n.Publisher
    target_type = n.Author
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=True,
            on_error=on_error,
            **kwargs,
        )

    def get_attr(self):
        pass

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)

    def get_update(self):
        pass


class Referenced(Edge):
    """
    e.g. News referenced stock yesterday
    """

    tense = Tense.Past
    aspect = Aspect.Simple
    source_type = n.News
    target_type = n.Equity
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=False,
            on_error=on_error,
            **kwargs,
        )

    def get_attr(self):
        pass

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)


class Influences(Edge):
    """
    e.g. Stock has been volatile since news published
    """

    tense = Tense.Present
    aspect = Aspect.Perfect
    source_type = n.News
    target_type = n.Equity
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=True,
            on_error=on_error,
            **kwargs,
        )

    def get_attr(self):
        pass

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)

    def get_update(self):
        pass


class Holds(Edge):
    """
    e.g. Position A holds 100 shares of B
    """

    tense = Tense.Present
    aspect = Aspect.Simple
    source_type = n.Position
    target_type = n.Equity
    tensor_dim = 10  # Placeholder

    def __init__(
        self,
        source: Hashable,
        target: Hashable,
        on_error: str = "omit",
        **kwargs,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            mutable=True,
            on_error=on_error,
            **kwargs,
        )

    def get_attr(self):
        pass

    def get_tensor(self):
        return torch.rand(self.tensor_dim, dtype=torch.float)

    def get_update(self):
        pass