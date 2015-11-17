from appium_selector.CapGenerators.Caps import Caps, propertyFromString


class GridWeb(Caps):

    def __init__(self, environment):
        self.env = environment
        self.options = {}
        self.caps = {}

    def displayString(self):
        platform = propertyFromString('platform', self.env)
        browser = propertyFromString('browserName', self.env)
        osv = propertyFromString('version', self.env)
        return "%s -- %s -- %s" % (platform, browser, osv)

    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'gridWeb'
        self.options['manufacturer'] = propertyFromString('platform', self.env)
        self.options['model'] = propertyFromString('browserName', self.env)
        self.options['osv'] = 'Local'
        self.options['mustard'] = mustard

        self.caps['platformName'] = propertyFromString('platform', self.env)
        self.caps['browserName'] = propertyFromString('browserName', self.env)
        self.caps['udid'] = self.displayString()
        self.caps['deviceName'] = self.displayString()
        self.caps['version'] = propertyFromString('version', self.env)
        return {'desiredCaps': self.caps, 'options': self.options}