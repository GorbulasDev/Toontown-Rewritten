from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.golf import GolfGlobals
import random

class DistributedGolfCourseAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGolfCourseAI")
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.avatars = []
        self.joinedAvatars = []
        self.holeIds = []
        self.courseId = 0
        self.chDoId = 0
    
    def generate(self):
        self.cInfo = GolfGlobals.CourseInfo[self.courseId]
        #while len(self.holeIds) != cInfo['numHoles']:
        #    newHole = random.choice(cInfo[

    def setGolferIds(self, avIds):
        self.avatars = avIds
        
    def d_setGolferIds(self, avIds):
        self.sendUpdate('setGolferIds', [avIds])
    
    def b_setGolferIds(self, avIds):
        self.setGolferIds(avIds)
        self.d_setGolferIds(avIds)
        
    def getGolferIds(self):
        return self.avatars

    def setCourseId(self, courseId):
        self.courseId = courseId
        
    def d_setCourseId(self, courseId):
        self.sendUpdate('setCourseId', [courseId])
        
    def b_setCourseId(self, courseId):
        self.setCourseId(courseId)
        self.d_setCourseId(courseId)
        
    def getCourseId(self):
        return self.courseId

    def setAvatarJoined(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.avatars:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to join a golf game they\'re not in!')
            return
        if avId in self.joinedAvatars:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to join a golf course twice!')
            return
        self.joinedAvatars.append(avId)
        if set(self.avatars) == set(self.joinedAvatars):
            pass

    def setAvatarReadyCourse(self):
        pass

    def setAvatarReadyHole(self):
        pass

    def setAvatarExited(self):
        pass

    def setCurHoleIndex(self, chIndex):
        self.chIndex = chIndex
    
    def d_setCurHoleIndex(self, chIndex):
        self.sendUpdate('setCurHoleIndex', [chIndex])
        
    def b_setCurHoleIndex(self, chIndex):
        self.setCureHoleIndex(chIndex)
        self.d_setCurHoleIndex(chIndex)
        
    def getCurHoleIndex(self):
        return self.chIndex

    def setCurHoleDoId(self, chDoId):
        self.chDoId = chDoId
        
    def d_setCurHoleDoId(self, chDoId):
        self.sendUpdate('setCurHoleDoId', [chDoId])
        
    def b_setCurHoleDoId(self, chDoId):
        self.setCurHoleDoId(chDoId)
        self.d_setCurHoleDoId(chDoId)
        
    def getCurHoleDoId(self):
        return self.chDoId

    def setDoneReward(self):
        pass

    def setReward(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9):
        pass

    def setCourseReady(self, todo0, todo1, todo2):
        pass

    def setHoleStart(self, todo0):
        pass

    def setCourseExit(self):
        pass

    def setCourseAbort(self, todo0):
        pass

    def setPlayHole(self):
        pass

    def avExited(self, todo0):
        pass

    def setScores(self, todo0):
        pass

    def changeDrivePermission(self, todo0, todo1):
        pass
        
    def calcCoursePar(self):
        retval = 0
        for holeId in self.holeIds:
            holeInfo = GolfGlobals.HoleInfo[holeId]
            retval += holeInfo['par']

        return retval
