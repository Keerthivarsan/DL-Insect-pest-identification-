Insect Pest Image Detection and Classification using Deep Learning
By: Kavitha S, Keerthivarsan D, Kodisumith R, Madhan V
Institution: Nandha Engineering College, Department of AI & DS

Agriculture is one of the most vital pillars of human survival and economic stability, especially in countries where a significant portion of the population depends directly on farming for their livelihood. Yet, one of the biggest threats to agricultural productivity comes from tiny, often invisible enemies: insect pests. These pests are responsible for over 40% of the total crop losses worldwide every year, affecting food supply, farmer income, and national economies.

Traditionally, identifying and managing insect pests required the expertise of agricultural specialists and entomologists, making the process time-consuming and inaccessible to many farmers. With the rapid advancement in Artificial Intelligence and Computer Vision technologies, there's now an opportunity to create smart, scalable, and efficient systems that can automate pest detection — even in real-time.

In this project, we developed a deep learning-based insect pest detection and classification system using the Faster R-CNN framework integrated with EfficientNet architectures (B4 and B7). The model was trained and tested on the IP102 dataset, one of the largest public datasets for pest classification, containing over 75,000 annotated images across 102 species of pests.

To address the challenges posed by unbalanced datasets and diverse pest appearances across different life stages, we applied advanced image preprocessing techniques, including resizing, normalization, and data augmentation methods such as flipping, zooming, and rescaling. This helped us increase the robustness of the model and reduce overfitting.

Our model pipeline begins with EfficientNet (B4 and B7) as a feature extractor, which processes pest images and generates high-quality feature maps. These are then passed to a Region Proposal Network (RPN), which identifies potential pest locations. The Region of Interest (ROI) pooling and final classification layers determine the pest class and draw bounding boxes around them.

We evaluated our system on three different configurations — using 5, 10, and 15 pest classes. The results were outstanding:

99.00% accuracy for 5 pest classes

96.00% accuracy for 10 pest classes

93.00% accuracy for 15 pest classes

These results not only surpassed several existing benchmarks like SSD-MobileNet and ResNet-based Faster R-CNN models but also demonstrated lower inference time and higher computational efficiency — making our solution ideal for real-world deployment in edge devices or mobile applications.

We also evaluated the performance using standard classification metrics such as Precision, Recall, F1-Score, and IoU (Intersection over Union) for bounding box accuracy. The system performed consistently well across all metrics, indicating its ability to correctly detect and classify pests even in images with complex backgrounds.

In conclusion, our work shows that deep learning, especially using architectures like Faster R-CNN with EfficientNet, holds immense promise in revolutionizing pest monitoring in agriculture. This solution can empower farmers with timely insights, reduce reliance on chemical pesticides, improve crop health, and ultimately support sustainable farming practices. Future directions for this work include expanding the model to cover all 102 pest classes in the IP102 dataset and integrating it into a mobile app or IoT-based monitoring system for real-time use in farms.
