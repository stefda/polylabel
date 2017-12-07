# polylabel (python port) [![Build Status](https://travis-ci.org/stefda/polylabel.svg?branch=master)](https://travis-ci.org/stefda/polylabel)

A fast algorithm for finding polygon pole of inaccessibility, the most distant internal point from the polygon outline (not to be confused with centroid), implemented as a Python library. Useful for optimal placement of a text label on a polygon.

Read all the detail including its JS and C++ implementation in the [original Mapbox repo](https://github.com/mapbox/polylabel).

## Usage

Given polygon coordinates in GeoJSON-like format and precision (1.0 by default), Polylabel returns the pole of inaccessibility coordinate in [x, y] format.

```python
p = polylabel(polygon, 1.0)
```
