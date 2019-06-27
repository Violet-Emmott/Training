class Tag(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.on_things = []
        
    def on_thing(self, thing):
        self.on_things.append(thing)
        
        

class Thing(object):
    def __init__(self, name, *tags, **kw):
        self.name = name
        self.tags = tags
        for tag in tags:
            tag.on_thing(self)
            
if __name__ == '__main__':
    tag1 = Tag('tag1', 'This is tag 1')
    tag2 = Tag('tag2', 'This is tag 2')
    tag3 = Tag('tag3', 'This is tag 3')
    
    thing1 = Thing('Thing1', tag1, tag2)
    thing2 = Thing('Thing2', tag2, tag3)
    thing3 = Thing('Thing3', tag3, tag1)
    
    for thing in tag1.on_things:
        print(thing.name)