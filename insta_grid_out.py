import sys
import ffmpeg

args = sys.argv

file = args[1]
row = int(args[2])
col = int(args[3])

print(file)
stream = ffmpeg.input(file)

probe = ffmpeg.probe(file)
image_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')

iw = int(image_info['width'])
ih = int(image_info['height'])

for r in range(row):
    for c in range(col):
        stream = ffmpeg.input(file)
        stream = ffmpeg.crop(stream,iw/col*c,ih/row*r,iw/col,ih/row)
        stream = ffmpeg.output(stream, 'out'+str(r)+'_'+str(c)+'.jpg')
        ffmpeg.run(stream)