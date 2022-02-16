class SimpleController(LightsController):

    def __init__(self, num_lights, color_on, color_off):
        super.self.init()


    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)
        
        super.lightSwitch(state)
