from appium_selector.CapGenerators.Caps import Caps, propertyFromString
from appium_selector.Helpers.GetDeviceInfo import getDeviceInfo


class GridMobileWeb(Caps):

    def __init__(self, environment):
        self.env = environment
        self.udid = propertyFromString('deviceName', self.env)
        self.platform = propertyFromString('platform', self.env)
        self.device = getDeviceInfo(self.udid, self.platform)
        self.options = {}
        self.caps = {}


    def displayString(self):
        platform = self.device['platform']
        udid = self.device['udid']
        name = self.device['name']
        browser = propertyFromString('browserName', self.env)
        return "%s -- %s -- %s -- %s" % (platform, udid, name, browser)
    
    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'gridMobileWeb'
        self.options['manufacturer'] = self.device['platform']
        self.options['model'] = propertyFromString('browserName', self.env)
        self.options['osv'] = self.device['osv']
        self.options['mustard'] = mustard

        self.caps['platform'] = propertyFromString('platform', self.env)
        self.caps['platformName'] = propertyFromString('platform', self.env)
        self.caps['browserName'] = propertyFromString('browserName', self.env)
        self.caps['udid'] = self.device['udid']
        self.caps['deviceName'] = self.device['udid']

        return {'desiredCaps': self.caps, 'options': self.options}