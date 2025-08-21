class Pet:
    all = []
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type. Must be one of {', '.join(self.PET_TYPES)}")

        self.name = name
        self.pet_type = pet_type
        
        # KEY FIX: Set the owner attribute on the Pet object first
        self.owner = owner
        
        # Then, if an owner was provided, call their method to add this pet
        if owner:
            owner.add_pet(self)

        self.all.append(self)
    
    def __repr__(self):
        return f"Pet(name='{self.name}', type='{self.pet_type}')"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Argument must be an instance of the Pet class")
        
        # This check now works because pet.owner has already been set in Pet.__init__
        if pet.owner is not None and pet.owner is not self:
            raise ValueError("Pet already has an owner")

        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name='{self.name}')"