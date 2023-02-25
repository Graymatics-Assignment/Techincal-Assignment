import argparse

import cv2
import numpy as np
import tensorflow as tf


def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)

    return graph


def read_tensor_from_frame(frame,
                           input_height=299,
                           input_width=299,
                           input_mean=0,
                           input_std=255):
    float_caster = tf.cast(frame, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.compat.v1.Session()
    return sess.run(normalized)


def load_labels(label_file):
    with open(label_file, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    model_file = "tensorflow/examples/label_image/data/inception_v3_2016_08_28_frozen.pb"
    label_file = "tensorflow/examples/label_image/data/imagenet_slim_labels.txt"
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "input"
    output_layer = "InceptionV3/Predictions/Reshape_1"
    confidence_threshold = 0.8

    parser = argparse.ArgumentParser()
    parser.add_argument("--video", help="video file to be processed")
    parser.add_argument("--graph", help="graph/model file to be executed")
    parser.add_argument("--labels", help="name of file containing labels")
    parser.add_argument("--input_height", type=int, help="input height")
    parser.add_argument("--input_width", type=int, help="input width")
    parser.add_argument("--input_mean", type=int, help="input mean")
    parser.add_argument("--input_std", type=int, help="input std")
    parser.add_argument("--input_layer", help="name of input layer")
    parser.add_argument("--output_layer", help="name of output layer")
    args = parser.parse_args()

    if args.graph:
        model_file = args.graph
    if args.labels:
        label_file = args.labels
    if args.input_height:
        input_height = args.input_height
    if args.input_width:
        input_width = args.input_width
    if args.input_mean:
        input_mean = args.input_mean
    if args.input_std:
        input_std = args.input_std
    if args.input_layer:
        input_layer = args.input_layer
    if args.output_layer:
        output_layer = args.output_layer

    graph = load_graph(model_file)
    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    labels = load_labels(label_file)

    cap = cv2.VideoCapture(args.video)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        t = read_tensor_from_frame(
            frame,
            input_height=input_height,
            input_width=input_width,
            input_mean=input_mean,
            input_std=input_std)

        with tf.compat.v1.Session(graph=graph) as sess:
            predictions = sess.run(output_operation.outputs[0], {
            input_operation.outputs[0]: t
            })
        
        top_index = np.argmax(predictions)
        label = labels[top_index]
        confidence = predictions[top_index]

        # Draw the label on the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        if confidence > 0.8:
            color = (0, 255, 0)  # Green
        else:
            color = (0, 0, 255)  # Red
        cv2.putText(frame, label, (10, 30), font, 1, color, 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()



