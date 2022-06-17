# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:41:37 2022

@author: solis
"""
from os.path import dirname, exists
import matplotlib as mpl
import matplotlib.pyplot as plt


def fig_size_cm_2_in(x_cm, y_cm=None):
    """
    sets x and y figure size in inches

    Parameters
    ----------
    x_cm : float
        x figure size in cm
    y_cm : float, optional
        Y figure size in cm. The default is None.

    Returns
    -------
    x_in : float
        x figure size in inches
    y_in : float
        y figure size in inches
    """
    # figure default size is 6.4 * 4.8
    default_ratio = 6.4 / 4.8

    x_in = x_cm / 2.54
    if y_cm is None:
        y_in = x_in / default_ratio
    else:
        y_in = y_cm / 2.54
    return x_in, y_in


def set_fig_parameters(x_in=6.4, y_in=4.8,
                       adjust_hspace=0.1, adjust_bottom=0.16, adjust_top=0.87,
                       defaults=True):
    """
    add parameters as you need them

    Returns
    -------
    None.

    """
    mpl.rcdefaults()
    if defaults:
        return
    plt.rc('figure', figsize=(x_in, y_in), dpi=80)
    plt.rc('font', size=8)
    plt.rc('axes', labelsize=8, titlesize= 9, grid=True)
    plt.rc('axes.spines', right=False, top=False)
    plt.rc('xtick', direction='out', top=False)
    plt.rc('ytick', direction='out', right=False)
    plt.rc('lines', linewidth=0.8, linestyle='-', marker='.', markersize=4)
    plt.rc('legend', fontsize=8, framealpha=0.5, loc='best')

    plt.subplots_adjust(hspace=adjust_hspace, bottom=adjust_bottom,
                        top=adjust_top)


def stem_1(x, y, str_title, str_ylabel, markerfmt=' ', basefmt=' ',
           close_plt=True ):
    if close_plt:
        plt.close()
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.stem(x, y, markerfmt=markerfmt, basefmt=basefmt)
    ax.set_title(str_title)
    plt.ylabel(str_ylabel)
    plt.tight_layout()
    plt.show()


def subplot_nv(x, y, legends, title, ylabels, plot=[],
               hspace=0.1, close_plt=True, fout=None):
    """
    Draw n graphs in the same figure of n time series.
    The graphs: are vertically aligned; share the x-axis

    Parameters
    ----------
    x : [[date]]
        x data values.
    y : [[float]]
        y data values.
    legends : [str]
        one legend of each date series.
    title : str
        Upper figure title.
    ylabels : [str]
        One label for each data series.
    plot : [bool], optional
        if i true, graph is of type plot, else type stem.
    hspace : float, optional
        vertical spaces between axes. The default is 0.1.
    close_plt : bool, optional
        if True close.plt() is executed before plot is drawn.
        The default is True.
    fout : str, optional
        Name of the output png file.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if fout is not None:
        d = dirname(fout)
        if not exists(d):
            raise ValueError(f'{d} no existe')

    n = len(x)
    if n != len(y) or n != len(legends) or n!= len(ylabels):
        raise ValueError('Arrays must have the same length')

    if close_plt:
        plt.close()

    if len(plot) != len(legends):
        plot = [True for i in range(len(legends))]
        plot[-1] = False

    colors = plt.rcParams["axes.prop_cycle"]()

    plt.subplots_adjust(hspace=hspace)

    fig, ax = plt.subplots(n, 1, sharex=True)
    fig.autofmt_xdate()
    fig.suptitle(title, fontsize=9)

    for i in range(n):
        if len(x[i]) != len(y[i]):
            raise ValueError(f'x, y arrays {i:d} have different length')
        clr = next(colors)["color"]
        if n == 1:
            oax = ax
        else:
            oax = ax[i]
        if plot[i]:
            oax.plot(x[i], y[i], marker=' ', label=legends[i], color=clr)
        else:
            oax.stem(x[i], y[i], clr, markerfmt=' ', basefmt=' ',
                       label=legends[i])
        oax.legend()
        oax.set(ylabel=ylabels[i])
    plt.tight_layout()
    if fout is None:
        plt.show()
    if fout is not None:
        plt.savefig(fout)


def subplot_1graph(x, y, legends, title, ylabel, close_plt=True, fout=None):
    """
    Draw 1 graph of n time series.

    Parameters
    ----------
    x : [[date]]
        x data values.
    y : [[float]]
        y data values.
    legends : [str]
        one legend of each date series.
    title : str
        Upper figure title.
    ylabel : str
        One common label for y axis.
    close_plt : bool, optional
        if True close.plt() is executed before plot is drawn.
        The default is True.
    fout : str, optional
        Name of the output png file.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if fout is not None:
        d = dirname(fout)
        if not exists(d):
            raise ValueError(f'{d} no existe')

    n = len(x)
    if n != len(y) or n != len(legends):
        raise ValueError('Arrays must have the same length')

    if close_plt:
        plt.close()

    colors = plt.rcParams["axes.prop_cycle"]()

    fig, ax = plt.subplots(1, 1)
    fig.autofmt_xdate()
    fig.suptitle(title, fontsize=9)

    for i in range(n):
        if len(x[i]) != len(y[i]):
            raise ValueError(f'x, y arrays {i:d} have different length')
        clr = next(colors)["color"]
        ax.plot(x[i], y[i], marker=' ', label=legends[i], color=clr)
        ax.legend()
    ax.set(ylabel=ylabel)
    plt.tight_layout()
    if fout is None:
        plt.show()
    if fout is not None:
        plt.savefig(fout)
