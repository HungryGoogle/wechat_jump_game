import cv2
import aircv as ac

# print circle_center_pos
def draw_circle(img, pos, circle_radius, color, line_width):
    cv2.circle(img, pos,  circle_radius, color, line_width)
    cv2.imshow('objDetect', imsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    imsrc = ac.imread('src_pic.jpg')
    imobj = ac.imread('object.png')

    # find the match position
    pos = ac.find_template(imsrc, imobj)
    circle_center_pos = pos['result']

    circle_center_pos = (int(circle_center_pos[0]), int(circle_center_pos[1]))

    circle_radius = 50
    color = (0, 255, 0)
    line_width = 3

    print(pos)

    # draw circle
    draw_circle(imsrc, circle_center_pos, circle_radius, color, line_width)