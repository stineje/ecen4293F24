import torch

model = torch.nn.Linear(10, 10).cuda()  # Example model on GPU
optimizer = torch.optim.Adam(model.parameters())

# Dummy input data
inputs = torch.randn(32, 10).cuda()
labels = torch.randn(32, 10).cuda()

# Use AMP for mixed precision training
scaler = torch.cuda.amp.GradScaler()

for epoch in range(5):
    optimizer.zero_grad()

    # Automatic mixed precision
    with torch.cuda.amp.autocast():
        outputs = model(inputs)
        loss = torch.nn.functional.mse_loss(outputs, labels)

    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()

    print(f"Epoch {epoch+1}, Loss: {loss.item()}")
