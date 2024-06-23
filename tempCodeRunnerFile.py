
# import os

# def correct_paths(file_path):
#     with open(file_path, 'r') as f:
#         lines = f.readlines()

#     corrected_lines = [line.replace('\\', '/') for line in lines]

#     with open(file_path, 'w') as f:
#         f.writelines(corrected_lines)

# # Paths to the text files
# train_txt_path = "D:/College/vdvw/juvdv2-vdvwc-main/train.txt"
# val_txt_path = "D:/College/vdvw/juvdv2-vdvwc-main/val.txt"

# # Correct the paths in the files
# correct_paths(train_txt_path)
# correct_paths(val_txt_path)

# print("Paths corrected in train.txt and val.txt")

# Example of how to debug the assigner method
class v8DetectionLoss:
    def assigner(self, preds, batch):
        # Example of potential indexing issue
        # Simulate the error condition
        try:
            _, target_bboxes, target_scores, fg_mask, _ = self.assigner(preds, batch)
        except IndexError as e:
            print(f"IndexError occurred: {e}")
            # Add debugging prints here to inspect preds, batch, and other variables

loss_fn = v8DetectionLoss()
loss_fn.assigner(preds, batch)  # Call the method with your actual data
