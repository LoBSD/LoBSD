#!python36

#
# Copyright (c) 2016 Erik Nordstrøm <erikn@LoBSD.org>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

import math
import sys

#
# BEGIN USER-SETABLE ----------------------------------------------------------
#

uz = \
{
    'near':
    {
        'h': 300.,
        's':  80.,
        'v': 100.
    },
    'far':
    {
        'h': 200.,
        's':  36.,
        'v': 100.
    }
}

st = 100 # Total number of steps

#
# END USER-SETABLE ------------------------------------------------------------
#

# Normalized
nz = \
{
    'near':
    {
        'hx': math.cos(uz['near']['h'] * math.pi / 180.),
        'hy': math.sin(uz['near']['h'] * math.pi / 180.),
        's':  uz['near']['s'] / 100.,
        'v':  uz['near']['v'] / 100.
    },
    'far':
    {
        'hx': math.cos(uz['far']['h'] * math.pi / 180.),
        'hy': math.sin(uz['far']['h'] * math.pi / 180.),
        's':  uz['far']['s'] / 100.,
        'v':  uz['far']['v'] / 100.
    }
}

def vec (nf):

    return \
    {
        'dhx': nf['far']['hx'] - nf['near']['hx'],
        'dhy': nf['far']['hy'] - nf['near']['hy'],
        'ds':  nf['far']['s'] - nf['near']['s'],
        'dv':  nf['far']['v'] - nf['near']['v']
    }

rz = vec(nz)

# Header to stderr

print("\t| {:^7s} | {:^7s} | {:^7s} | {:^7s}".\
    format("H_x", "H_y", "S", "V"), file=sys.stderr)

valfmt = "\t| {:+7.2f} | {:+7.2f} | {:+7.2f} | {:+7.2f}"

# Core data to stderr

print("-" * 80, file=sys.stderr)

print("   near" + valfmt.\
    format(nz['near']['hx'],
           nz['near']['hy'],
           nz['near']['s'],
           nz['near']['v']),
    file=sys.stderr)

print("    vec" + valfmt.\
    format(rz['dhx'],
           rz['dhy'],
           rz['ds'],
           rz['dv']),
    file=sys.stderr)

print("    far" + valfmt.\
    format(nz['far']['hx'],
           nz['far']['hy'],
           nz['far']['s'],
           nz['far']['v']),
    file=sys.stderr)

print("-" * 80, file=sys.stderr)

# Data to stdout

for i in range(0, st):

    cdzhx, cdzhy, cdzs, cdzv = \
        [m * float(i) / st for m in \
            [rz['dhx'], rz['dhy'], rz['ds'], rz['dv']]]

    print(valfmt.format(\
        nz['near']['hx'] + cdzhx,
        nz['near']['hy'] + cdzhy,
        nz['near']['s']  + cdzs,
        nz['near']['v']  + cdzv))
