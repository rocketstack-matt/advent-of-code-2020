from __future__ import annotations


class Bag:
    name_contents_marker = 'bags contain'
    empty_bag_marker = 'no other bags.'

    def __init__(self, rule) -> None:
        super().__init__()
        self.name = rule[0:rule.find(self.name_contents_marker)-1]
        self.contents = set()

        rules = [x.strip() for x in rule[rule.find(self.name_contents_marker) +
                                         len(self.name_contents_marker):len(rule)].split(',')]
        if self.empty_bag_marker in rules:
            rules.remove(self.empty_bag_marker)

        for rule in rules:
            count = int(rule[0])
            bag = rule[2:rule.rfind(' ')].strip()
            self.contents.add((count, bag))

    def find_containers(self, bag_dict: dict[Bag]):
        bags = []
        for key in bag_dict:
            if key==self.name:
                bags+=(bag_dict[key])
                for bag in bag_dict[key]:
                    bags+=bag.find_containers(bag_dict)
        return set(bags)

    def find_contents(self, bag_dict: dict[Bag]):
        total=0
        for count, name in self.contents:
            total+=count
            total+=count*bag_dict[name].find_contents(bag_dict)
            
        return total

    def __str__(self):
        string = 'name: ' + self.name
        if len(self.contents) > 0:
            string += ' {'
            for count, name in self.contents:
                string += str(count) + ': ' + name + ', '
            string = string[0:len(string)-2]
            string += '}'
        return string

    def __repr__(self):
        return self.__str__()
