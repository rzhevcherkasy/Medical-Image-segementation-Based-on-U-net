import cv2
import scipy.misc

import SimpleITK as sitk  # reading MR images

import glob

import imageio


def dealdata(readfolderT, readfolderL, datapathlabel,datapathimg, TrainingImagesList, TrainingLabelsList):

    y_folder = readfolderT
    yread = sitk.ReadImage(y_folder)
    yimage = sitk.GetArrayFromImage(yread)
    x = yimage[:184, :232, 112:136]
    x = scipy.rot90(x)
    x = scipy.rot90(x)
    for j in range(x.shape[2]):
        TrainingImagesList.append((x[:184, :224, j]))


    y_folder = readfolderL
    yread = sitk.ReadImage(y_folder)
    yimage = sitk.GetArrayFromImage(yread)
    x = yimage[:184, :232, 112:136]
    x = scipy.rot90(x)
    x = scipy.rot90(x)
    for j in range(x.shape[2]):
        TrainingLabelsList.append((x[:184, :224, j]))

    for i in range(len(TrainingImagesList)):
        xchangeL = TrainingImagesList[i]
        xchangeL = cv2.resize(xchangeL, (128, 128))
        imageio.imwrite(datapathimg + str(i) + '.png', xchangeL)
    for i in range(len(TrainingLabelsList)):
        xchangeL = TrainingLabelsList[i]
        xchangeL = cv2.resize(xchangeL, (128, 128))
        imageio.imwrite(datapathlabel + str(i) + '.png', xchangeL)
    return TrainingLabelsList,TrainingLabelsList
