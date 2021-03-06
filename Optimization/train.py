import numpy as np
import datetime
from sklearn import preprocessing
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor
import mysql.connector
import datetime as dt
import constants
import models

def getDate(day, month, year, cursor):
    gameIDP = 0

    findGame = "SELECT iddates FROM dates WHERE date = %s"
    findGameData = (dt.date(year, month, day),)
    cursor.execute(findGame, findGameData)

    for game in cursor:
        gameIDP = game[0]

    return gameIDP

def train(dateID, cursor, cnx):
    print "Training Ben Simmons Model..."


    benSimmonsModel = models.benSimmonsModel

    getFeaturesB = "SELECT "

    for m in (benSimmonsModel):
        getFeaturesB += m
        getFeaturesB += ", "
    getFeaturesB = getFeaturesB[:-2]
    getFeaturesB += " FROM features"    # turn into numpy arrays
    getFeaturesB += " WHERE dateID < "
    getFeaturesB += str(dateID)
    getFeaturesB += " and fanduelPts > 0;"

    allPlayerFeatures = []

    cursor.execute(getFeaturesB)

    features = cursor.fetchall()
    for feat in features:
        allPlayerFeatures.append(list(feat))

    FDTargets = []

    getTargets = "SELECT fanduelPts FROM features WHERE dateID < %s and fanduelPts > 0;"
    getTargetsData = (dateID,)
    cursor.execute(getTargets, getTargetsData)
    targets = cursor.fetchall()

    for tar in targets:
        FDTargets.append(float(tar[0]))

    numFeatures = len(allPlayerFeatures[0])
    testXB = np.asarray(allPlayerFeatures)
    testY = np.asarray(FDTargets)

    predictTest = [allPlayerFeatures[4]]
    predictTest.append(allPlayerFeatures[5])
    predXB = np.asarray(predictTest)

    print "Number of training examples: " + str(np.shape(testXB)[0])

    # add bias term
    ones = np.ones((np.shape(testXB)[0], 1), dtype=float)
    testXB = np.hstack((ones, testXB))

    ones = np.ones((np.shape(predXB)[0], 1), dtype=float)
    predXB = np.hstack((ones, predXB))
    #print testY
    alph = .00047
    clf = MLPRegressor(solver='lbfgs', alpha=alph,hidden_layer_sizes=(18, 54), random_state=1)
    clf.fit(testXB, testY)
    fit = clf.score(testXB, testY)
           


   

    alpha = .00001    
    ridge = Ridge(alpha=alpha, fit_intercept=False, normalize=False, max_iter=100000)
    ridge.fit(testXB, testY)
    print alpha, ridge.score(testXB, testY)
    print alpha, clf.score(testXB, testY)
    print clf.predict(predXB)
    print ridge.predict(predXB)
    
    thetaSKLearnRidge = ridge.coef_
    fileName = 'coef' + "Ben" + '.npz'

    outfile = open(fileName, 'w')
    np.save(outfile, thetaSKLearnRidge)

    thetaSKLearnRidge =  clf.coefs_
    fileName = 'coef' + "NueralNetwork" + '.npz'

    outfile = open(fileName, 'w')
    np.save(outfile, thetaSKLearnRidge)
    return clf

if __name__ == "__main__":

    # dates to retrieve data for batter test data
    # start date
    cnx = mysql.connector.connect(user=constants.testUser,
            host=constants.testHost,
            database=constants.testName,
            password=constants.testPassword)                                                                                                               
    cursor = cnx.cursor()

    now = datetime.datetime.now() - datetime.timedelta(days=1)
  
    dateID = getDate(now.day, now.month, now.year, cursor)

    train(dateID, cursor, cnx)

    cnx.commit()
    cnx.close()
 
