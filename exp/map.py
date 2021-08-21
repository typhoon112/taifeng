import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter, LatitudeLocator
import json


plt.rcParams["font.size"] = 9 # 设置显示字体大小
plt.tick_params(labelsize=9) # 设置坐标轴字体大小
plt.rcParams["font.family"] = "Verdana" # 设置默认字体

def map1():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())
    ax.set_extent((104, 133, 10, 45))
    ax.add_geometries(Reader("shp/ne_10m_land.shp").geometries(), ccrs.PlateCarree(), facecolor="none", edgecolor="#808080", linewidth=0.5)
    ax.add_geometries(Reader("shp/ne_50m_lakes.shp").geometries(), ccrs.PlateCarree(), facecolor="none", edgecolor="#808080", linewidth=0.5)
    lb = ax.gridlines(draw_labels=None, x_inline=False, y_inline=False, linewidth=0.1, color="gray", alpha=0.8, linestyle="--")
    lb.xlocator = mticker.FixedLocator(range(0, 180, 10))
    lb.ylocator = mticker.FixedLocator(range(0, 90, 10))
    lb = ax.gridlines(draw_labels=True, x_inline=False, y_inline=False, linewidth=0.1, color="gray", alpha=0.8, linestyle="--")
    lb.top_labels = False
    lb.right_labels = None
    lb.ylabel_style = {"size": 10, "color": "k"}
    lb.xlabel_style = {"size": 10, "color": "k"}
    lb.rotate_labels = False
    with open("zjwater2019_2020.json") as f:
        tf = json.load(f)
    for tfid in ["A.202018(Base)", "B.202022(SP=82.6%)", "C.202007(SP=68.3%)", "D.202004(SP=50.7%)", "E.202008(SP=44.6%)", "F.201909(SP=32.2%)"]:
        if "Base" in tfid:
            plt.plot([x[0] for x in tf[tfid[2:8]]], [x[1] for x in tf[tfid[2:8]]], color="k", linewidth=1.5, transform=ccrs.PlateCarree(), label=tfid[0] + tfid[8:])
        else:
            plt.plot([x[0] for x in tf[tfid[2:8]]], [x[1] for x in tf[tfid[2:8]]], linewidth=1.1, transform=ccrs.PlateCarree(), label=tfid[0] + tfid[8:])
    plt.legend(fontsize=10)
    # plt.show()
    plt.savefig("map1.png", dpi=300, bbox_inches="tight")

def map2():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())
    ax.set_extent((116, 148, 11, 49.5))
    ax.add_geometries(Reader("shp/ne_10m_land.shp").geometries(), ccrs.PlateCarree(), facecolor="none", edgecolor="#808080", linewidth=0.5)
    ax.add_geometries(Reader("shp/ne_50m_lakes.shp").geometries(), ccrs.PlateCarree(), facecolor="none", edgecolor="#808080", linewidth=0.5)
    lb = ax.gridlines(draw_labels=None, x_inline=False, y_inline=False, linewidth=0.1, color="gray", alpha=0.8, linestyle="--")
    lb.xlocator = mticker.FixedLocator(range(0, 180, 10))
    lb.ylocator = mticker.FixedLocator(range(0, 90, 10))
    lb = ax.gridlines(draw_labels=True, x_inline=False, y_inline=False, linewidth=0.1, color="gray", alpha=0.8, linestyle="--")
    lb.top_labels = False
    lb.right_labels = None
    lb.ylabel_style = {"size": 10, "color": "k"}
    lb.xlabel_style = {"size": 10, "color": "k"}
    lb.rotate_labels = False
    with open("zjwater2018_2020.json") as f:
        tf = json.load(f)
    for tfid in ["G.201909(Base)", "H.202010(SP=60.0%)", "I.201808(SP=59.9%)", "J.202009(SP=58.6%)"]:
        if "Base" in tfid:
            plt.plot([x[0] for x in tf[tfid[2:8]]], [x[1] for x in tf[tfid[2:8]]], color="k", linewidth=1.5, transform=ccrs.PlateCarree(), label=tfid[0] + tfid[8:])
        else:
            plt.plot([x[0] for x in tf[tfid[2:8]]], [x[1] for x in tf[tfid[2:8]]], linewidth=1.1, transform=ccrs.PlateCarree(), label=tfid[0] + tfid[8:])
    plt.legend(fontsize=10)
    # plt.show()
    plt.savefig("map2.png", dpi=300, bbox_inches="tight")

def map3():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())
    ax.set_extent((115, 138, 16, 40))
    ax.add_geometries(Reader("shp/ne_10m_land.shp").geometries(), ccrs.PlateCarree(), facecolor="none", edgecolor="#808080", linewidth=0.5)
    ax.add_geometries(Reader("shp/ne_50m_lakes.shp").geometries(), ccrs.PlateCarree(), facecolor="none", edgecolor="#808080", linewidth=0.5)
    ax.add_geometries(Reader("shp/china2.shp").geometries(), ccrs.PlateCarree(), facecolor="none", edgecolor="#808080", linewidth=0.5)
    lb = ax.gridlines(draw_labels=None, x_inline=False, y_inline=False, linewidth=0.1, color="gray", alpha=0.8, linestyle="--")
    lb.xlocator = mticker.FixedLocator(range(0, 180, 10))
    lb.ylocator = mticker.FixedLocator(range(0, 90, 10))
    lb = ax.gridlines(draw_labels=True, x_inline=False, y_inline=False, linewidth=0.1, color="gray", alpha=0.8, linestyle="--")
    lb.top_labels = False
    lb.right_labels = None
    lb.ylabel_style = {"size": 10, "color": "k"}
    lb.xlabel_style = {"size": 10, "color": "k"}
    lb.rotate_labels = False
    with open("zjwater2018_2021.json") as f:
        tf = json.load(f)
    colors = ["C" + str(i) for i in range(6)]
    colorid = 0
    cutoffs = [49, 40, 28, 41, 61]
    for tfid in ["K.202106(Base)", "L.201814(SP=95.0%)", "M.201917(SP=94.9%)", "N.201807(SP=92.1%)", "O.202004(SP=91.0%)", "P.201909(SP=90.6%)"]:
        if "Base" in tfid:
            plt.plot([x[0] for x in tf[tfid[2:8]]], [x[1] for x in tf[tfid[2:8]]], color="k", linewidth=1.5, transform=ccrs.PlateCarree(), label=tfid[0] + tfid[8:])
        else:
            plt.plot([x[0] for x in tf[tfid[2:8]][:cutoffs[colorid]]], [x[1] for x in tf[tfid[2:8]][:cutoffs[colorid]]], color=colors[colorid], linewidth=1.1, linestyle="-", transform=ccrs.PlateCarree(), label=tfid[0] + tfid[8:])
            plt.plot([x[0] for x in tf[tfid[2:8]][cutoffs[colorid]:]], [x[1] for x in tf[tfid[2:8]][cutoffs[colorid]:]], color=colors[colorid], linewidth=1.1, linestyle="--", transform=ccrs.PlateCarree())
            colorid += 1
    plt.legend(fontsize=10)
    # plt.show()
    plt.savefig("map3.png", dpi=300, bbox_inches="tight")

# map1()
# map2()
map3()