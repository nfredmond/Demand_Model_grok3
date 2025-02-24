import os
import cupy as cp
import numpy as np
import logging

logger = logging.getLogger(__name__)

def create_aequilibrae_project(project_id: int) -> str:
    project_dir = os.path.join("projects", f"project_{project_id}")
    os.makedirs(project_dir, exist_ok=True)
    project_path = os.path.join(project_dir, "aequilibrae_project.db")
    # Placeholder for AequilibraE project creation
    return project_path

def compute_trip_matrix(zones, use_chunking: bool = False) -> list:
    num_zones = len(zones)
    logger.info(f"Computing trip matrix for {num_zones} zones")
    
    try:
        with cp.cuda.Device(0):
            if use_chunking and num_zones > 500:
                chunk_size = 250
                trip_results = []
                for i in range(0, num_zones, chunk_size):
                    end = min(i + chunk_size, num_zones)
                    chunk_od = cp.random.random((end - i, num_zones)) * 100
                    chunk_sum = cp.sum(chunk_od, axis=1)
                    for j, value in enumerate(chunk_sum):
                        trip_results.append({"origin": i + j, "dest": i, "trips": float(value)})
                return trip_results
            else:
                od_matrix = cp.random.random((num_zones, num_zones)) * 100
                distributed = cp.dot(od_matrix, od_matrix.T)
                trip_results = []
                for i in range(num_zones):
                    trip_results.append({"origin": i, "dest": i, "trips": float(cp.sum(distributed[i]))})
                return trip_results
    except Exception as e:
        logger.error(f"GPU computation failed: {e}")
        od_matrix = np.random.random((num_zones, num_zones)) * 100
        distributed = np.dot(od_matrix, od_matrix.T)
        trip_results = []
        for i in range(num_zones):
            trip_results.append({"origin": i, "dest": i, "trips": float(np.sum(distributed[i]))})
        return trip_results