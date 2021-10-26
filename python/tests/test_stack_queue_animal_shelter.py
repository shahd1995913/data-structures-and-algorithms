
from stack_queue_animal_shelter.stack_queue_animal_shelter  import (Dog_animal, AnimalShelter, Cat_animal)

def test_dog():

    shelter = AnimalShelter()

    dog1 = Dog_animal("Ram")

    dog2 = Dog_animal("Jo")

    dog3 = Dog_animal("Li")

    dog4  = Dog_animal("kia")

    shelter.enqueue(dog1)

    shelter.enqueue(dog2)

    shelter.enqueue(dog3)

    shelter.enqueue(dog4)

    assert shelter.dog.front.value   == "Ram"

    shelter.dequeue("dog")

    assert shelter.dog.front.value == "Jo"




def test_cog():

    shelter = AnimalShelter()

    cat1 = Cat_animal("lili")

    cat2 = Cat_animal("tom")

    cat3 = Cat_animal("mik")

    cat4  = Cat_animal("nowa")

    shelter.enqueue(cat1)

    shelter.enqueue(cat2)

    shelter.enqueue(cat3)

    shelter.enqueue(cat4)

    assert shelter.cat.front.value   == "lili"

    shelter.dequeue("cat")

    assert shelter.cat.front.value == "tom"
