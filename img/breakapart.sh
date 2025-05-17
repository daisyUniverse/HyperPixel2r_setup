#!/bin/bash

sudo convert $1 -coalesce $2/frame_%03d.gif
