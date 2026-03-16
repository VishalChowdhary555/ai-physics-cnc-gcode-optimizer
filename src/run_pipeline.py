import os

from src.dataset_generator import generate_dataset
from src.preprocessing import preprocess
from src.train_models import train_catboost
from src.evaluate_models import evaluate
from src.ga_optimizer import optimize
from src.gcode_parser import parse_gcode
from src.gcode_regenerator import regenerate_gcode
from src.utils import save_model


def main():
    print("\n=== AI + Physics CNC Optimization Pipeline ===\n")

    # Create output folders if they do not exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    os.makedirs("results", exist_ok=True)
    os.makedirs("examples", exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Generate synthetic dataset
    # ------------------------------------------------------------------
    print("[1/7] Generating synthetic machining dataset...")
    df = generate_dataset(n_samples=5000)
    dataset_path = "data/synthetic_machining_dataset.csv"
    df.to_csv(dataset_path, index=False)
    print(f"Dataset saved to: {dataset_path}")

    # ------------------------------------------------------------------
    # 2. Preprocess dataset
    # ------------------------------------------------------------------
    print("\n[2/7] Preprocessing dataset...")
    X_train, X_test, y_train, y_test, scaler = preprocess(df)
    print("Preprocessing complete.")

    # ------------------------------------------------------------------
    # 3. Train ML model
    # ------------------------------------------------------------------
    print("\n[3/7] Training CatBoost model...")
    model = train_catboost(X_train, y_train)
    model_path = "models/catboost_model.pkl"
    save_model(model, model_path)
    print(f"Model saved to: {model_path}")

    # ------------------------------------------------------------------
    # 4. Evaluate model
    # ------------------------------------------------------------------
    print("\n[4/7] Evaluating model...")
    metrics = evaluate(model, X_test, y_test)
    print("Evaluation Results:")
    for key, value in metrics.items():
        print(f"  {key}: {value:.4f}")

    metrics_path = "results/model_metrics.txt"
    with open(metrics_path, "w") as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value:.6f}\n")
    print(f"Metrics saved to: {metrics_path}")

    # ------------------------------------------------------------------
    # 5. Run Genetic Algorithm optimization
    # ------------------------------------------------------------------
    print("\n[5/7] Running machining parameter optimization...")
    best_params = optimize(model)
    best_feed, best_depth = best_params
    print(f"Optimized Feed Rate: {best_feed:.2f}")
    print(f"Optimized Depth of Cut: {best_depth:.2f}")

    optimization_path = "results/optimized_parameters.txt"
    with open(optimization_path, "w") as f:
        f.write(f"Optimized Feed Rate: {best_feed:.6f}\n")
        f.write(f"Optimized Depth of Cut: {best_depth:.6f}\n")
    print(f"Optimized parameters saved to: {optimization_path}")

    # ------------------------------------------------------------------
    # 6. Parse original G-code
    # ------------------------------------------------------------------
    print("\n[6/7] Parsing original G-code...")

    original_gcode_path = "examples/original_pocket.gcode"

    if not os.path.exists(original_gcode_path):
        print(f"Warning: {original_gcode_path} not found.")
        print("Skipping G-code regeneration step.")
        return

    gcode = parse_gcode(original_gcode_path)
    print(f"Loaded {len(gcode)} lines of G-code.")

    # ------------------------------------------------------------------
    # 7. Regenerate optimized G-code
    # ------------------------------------------------------------------
    print("\n[7/7] Regenerating optimized G-code...")
    optimized_gcode = regenerate_gcode(
        gcode=gcode,
        new_feed=best_feed,
        new_depth=best_depth
    )

    optimized_gcode_path = "examples/optimized_pocket.gcode"
    with open(optimized_gcode_path, "w") as f:
        for line in optimized_gcode:
            f.write(line + "\n")

    print(f"Optimized G-code saved to: {optimized_gcode_path}")

    print("\n=== Pipeline completed successfully ===\n")


if __name__ == "__main__":
    main()
