def midPoint(x1, x2, y1, y2):
    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2
    return xMid, yMid
    
def generateMid(x1, x2, x3, y1, y2, y3):
    xMidL, yMidL = midPoint(x1, x2, y1, y2)
    xMidR, yMidR = midPoint(x3, x2, y3, y2)
    xMidM, yMidM = midPoint(xMidL, xMidR, yMidL, yMidR)
    return xMidL, xMidM, xMidR, yMidL, yMidM, yMidR

def generateBezierBF(arrX, arrY):
    xRes = []
    yRes = []
    xRes.append(arrX[0])
    yRes.append(arrY[0])
    for i in range (len(arrX)-2):
        xMidL, xMidM, xMidR, yMidL, yMidM, yMidR = generateMid(arrX[i], arrX[i+1], arrX[i+2], arrY[i], arrY[i+1], arrY[i+2])
        if i == 0:
            xRes.append(xMidL)
            yRes.append(yMidL)
        xRes.append(xMidM)
        yRes.append(yMidM)
        xRes.append(xMidR)
        yRes.append(yMidR)
    xRes.append(arrX[len(arrX)-1])
    yRes.append(arrY[len(arrY)-1])

    return xRes, yRes