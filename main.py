from abc import abstractmethod, ABC

class Vacancy(ABC):
    @abstractmethod
    def get_vacancy_count(self):
        pass

    @abstractmethod
    def set_vacancy_count(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def restore(self, memento):
        pass


class MementoVacancy(ABC):
    @abstractmethod
    def get_state(self):
        pass

class AbstractVaultJobs(ABC):
    @abstractmethod
    def save_state(self):
        pass

    @abstractmethod
    def get_previous_state(self):
        pass


class VaultJobs(AbstractVaultJobs):
    def __init__(self, _jobs: Vacancy):
        self.__vault_jobs = []
        self._jobs = _jobs

    def save_state(self, __state: MementoVacancy):
        self.__vault_jobs.append(__state)

    def get_previous_state(self):
        memento = self.__vault_jobs.pop()
        self._jobs.restore(memento)

    def show_history(self) -> list:
        return self.__vault_jobs


class MementoConcreteVacancy(MementoVacancy):
    def __init__(self, _state):
        self.__state = _state

    def get_state(self):
        return self.__state

    def __repr__(self):
        return f'<Number of vacancies: {self.__state} >'


class ConcreteVacancy(Vacancy):
    def __init__(self):
        self._vacancy_count = 10000

    def get_vacancy_count(self) -> int:
        return self._vacancy_count

    def set_vacancy_count(self, count: int):

        if abs(count) == count:
            self._vacancy_count = count

    def save(self) -> MementoVacancy:
        return MementoConcreteVacancy(self._vacancy_count)

    def restore(self, memento: MementoVacancy):
        self._vacancy_count = memento.get_state()
        print(f'Last number of vacancies: {self._vacancy_count}')


cv = ConcreteVacancy()
saver = VaultJobs(cv)
while True:
    ans = int(input("Select an action\n\t "
                "1. Set the number of new vacancies;\n\t "
                "2. Get the number of new vacancies;\n\t "
                "3. View the history of vacancies;\n\t "
                "4. View the previous number of vacancies sent;\n\t "
                "0. Exit\n\t"))
    if ans == 1:
        ch = int(input("Enter the number of vacancies: "))
        cv.set_vacancy_count(ch)
        saver.save_state(cv.save())
    if ans == 2:
        print(cv.get_vacancy_count())
    if ans == 3:
        print(saver.show_history())
    if ans == 4:
        saver.get_previous_state()
    if ans == 0:
        break