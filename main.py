import numpy as np
import cv2

img = np.full((1024, 1024, 3), 255, dtype=np.uint8)
cv2.imshow('image', img)
Key = 0
shape = []
thikness = 2
Color = (0,0,0)
i= 0
c= 0

Counter = 0
Number = []
number =0
while(1):
    cv2.imshow('image', img)
    def Snap_lenth(parameterA, parameterB):
        val = 0

        for i in range(len(old_Line)):
            XS_Lenth = parameterA[0][0] - parameterB[i][0]
            YS_Lenth = parameterA[0][1] - parameterB[i][1]
            SquS_X = abs(XS_Lenth) * abs(XS_Lenth)
            SquS_Y = abs(YS_Lenth) * abs(YS_Lenth)
            LenthS = ((SquS_Y + SquS_X) ** (0.5))
            if LenthS <= 20:
                print("Snap Start")
                val = 1
                break
            if len(old_Line) >= 2 and len(points) >= 2:
                XE_Lenth = parameterA[1][0] - parameterB[i][0]
                YE_Lenth = parameterA[1][1] - parameterB[i][1]
                SquE_X = abs(XE_Lenth) * abs(XE_Lenth)
                SquE_Y = abs(YE_Lenth) * abs(YE_Lenth)
                LenthE = ((SquE_Y + SquE_X) ** (0.5))

                if LenthE <= 20:
                    print("Snap End")
                    val = 2
                    break


        else:
            val = 0

        val2 = (val, i)
        print(val2)

        return val2
    def click_event(event, x, y ,flags, param) :
        global number
        global Counter
        cv2.imshow('image', img)
        if event == cv2.EVENT_RBUTTONDOWN:
            del old_Line[0]
            del old_Line[0]
            del Number[0]
            del shape[0]
            cv2.rectangle(img, (0,0),
                          (1024,1024), (255,255,255),
                          -1)
            print("S")

            for n in range(int(len(old_Line)/2)):
                print(old_Line)
                print("old_Line")
                print(shape)
                if shape[n] == 99:
                    cv2.circle(img, old_Line[2*(n)], int(Number[n]), Color, thikness)
                    cv2.putText(img, str(Number[n]), old_Line[2*(n)+1], cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 255, 0), 1, cv2.LINE_AA)
                elif  shape[n] == 108:

                    cv2.line(img, old_Line[2*(n)],old_Line[2*(n)+1], Color, thikness)
                    cv2.putText(img, str((Number[(n)])), old_Line[2*(n)], cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 255, 0), 1, cv2.LINE_AA)
                elif shape[n] == 107:
                    print('f')
            cv2.imshow('image', img)

        if event == cv2.EVENT_LBUTTONDOWN :
            points.append((x, y))

            if len(old_Line) >= 2 and len(points) >= 2:
                snapVal = Snap_lenth(points, old_Line)
                if snapVal[0]== 1:

                    points[0] = old_Line[snapVal[1]]
                    print("Start Snap")
                elif snapVal[0] == 2:

                    points[0] = old_Line[snapVal[1]]
                    print("End snap")



            if len(points) >= 2:
                Counter = Counter+1
                X_Lenth = points[0][0] - points[1][0]
                Y_Lenth = points[0][1] - points[1][1]
                Squ_X = abs(X_Lenth) * abs(X_Lenth)
                Squ_Y = abs(Y_Lenth) * abs(Y_Lenth)
                Lenth = ((Squ_Y + Squ_X) ** (0.5))
                old_lenth.append(Lenth)
                print(Lenth)
                XpositionVec = points[1][0] - points[0][0]
                YpositionVec = points[1][1] - points[0][1]
                XunitVec = XpositionVec / Lenth
                YunitVec = YpositionVec / Lenth

                if Key == 99: #c
                    shape.insert(0,Key)
                    if number >> 0:

                        cv2.circle(img, points[0], number, Color, thikness)

                        cv2.putText(img, str((number)), points[1], cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        Number.insert(0,number)
                        number = 0
                    else:
                        cv2.circle(img, points[0], int (Lenth), Color, thikness)
                        cv2.putText(img, str((Lenth)), points[1], cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        Number.insert(0, Lenth)

                elif Key == 108:
                    shape.insert(0,Key)
                    if number >> 0 :
                        cv2.line(img, points[0],(points[0][0]+int(number*XunitVec),points[0][1]+int(number*YunitVec)) , Color, thikness)
                        cv2.putText(img, str((number)), points[0], cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        Number.insert(0,number)
                        number = 0
                    else:
                        cv2.line(img, points[0], points[1], Color, thikness)
                        cv2.putText(img, str((Lenth)), points[0], cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        Number.insert(0, Lenth)
                elif Key == 107 :
                    shape.insert(0,Key)
                    if number >> 0:
                        cv2.rectangle(img, points[0],(points[0][0]+int(number*XunitVec),points[0][1]+int(number*YunitVec)), Color, thikness)
                        cv2.putText(img, str((number)), points[0], cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        points[1]=(points[0][0]+int(number*XunitVec),points[0][1]+int(number*YunitVec))
                        Number.insert(0,number)
                        number = 0

                    else:
                        cv2.rectangle(img, points[0],points[1], Color, thikness)
                        cv2.putText(img, str((Lenth)), points[0], cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 255, 0), 1, cv2.LINE_AA)
                        Number.insert(0,Lenth)
                old_Line.insert(0, points[0])
                old_Line.insert(1, points[1])
                cv2.imshow('image', img)
                print(shape)
                points.clear()

    old_lenth = []
    points = []
    cv2.imshow('image', img)
    old_Line = []
    cv2.rectangle(img, (1, 1), (70, 80), (255, 255, 255), -1)
    cv2.rectangle(img, (860, 1), (1024, 80), (255, 255, 255), -1)
    if number >= 48:
        cv2.putText(img, str(number), (900, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 0), 3, cv2.LINE_AA)



    cv2.setMouseCallback('image', click_event)
    Key = cv2.waitKey(0)
    cv2.imshow('image', img)
    print(Key)
    if Key == 115 : thikness = thikness -1 #s
    if Key == 119 : thikness = thikness +1 #w
    if Key == 98 : Color = (225,0 ,0)
    if Key == 114 :  Color = (0, 0,255)
    if Key == 103:  Color = (0, 255, 0)
    if (Key - 48 >= 0 and Key - 48 <= 9) :
            Number.append(Key - 48)
            i= i +1

            Key = -1

    else :
            print("this is not a number ")
            if Key == 13 :
                tenth = 1
                while i >> 0:
                    i = i - 1
                    number = number + Number[i] * tenth
                    print("The Number is")
                    print(number)
                    tenth = tenth *10

            Number.clear()


    if Key == 27:
        cv2.destroyAllWindows()
        break




