#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A simple example of assisilib usage, spawning two oval arenas
(assumes any CASUs required are spawned externally)

'''

from assisipy import sim
from assisipy_utils import arena
import argparse

from numpy import deg2rad

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=float, default=0.0)
    parser.add_argument('-y', type=float, default=0.0)
    parser.add_argument('-t', '--theta_deg', type=float, default=0.0)
    parser.add_argument('-l', '--label', type=str, default='popln1-')
    parser.add_argument('-o', '--output', type=str, default='valid.arena')
    args = parser.parse_args()

    # in the 9-CASU arena of V3 casus, the centres are 9cm apart, centred at 5
    # 9 8 7
    # 6 5 4
    # 3 2 1
    # ----/ --
    #   <door>
    #

    # define an arena wall object
    A = arena.StadiumArena(ww=0.5, label_stub=args.label+"-arena")
    T = arena.Transformation(dx=args.x, dy=args.y, theta=float(deg2rad(args.theta_deg)))
    A.transform(T)
    posns_to_write = [x for sublist in A.get_valid_zone() for x in sublist]

    A.write_bounds_spec(args.output)

    print "[I] wrote specification to {}".format(args.output)

    # now we have a definition, we can spawn the wall segments
    simctrl = sim.Control()
    A.spawn(simctrl)

