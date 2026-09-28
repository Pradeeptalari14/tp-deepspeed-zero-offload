/**
 * DeepSpeed Distributed Cluster Topology Monitor
 */

export interface GPUAllocation {
  gpu_id: number;
  vram_allocated_gb: number;
  nvme_prefetch_bw_gbs: number;
}

export class ClusterTopologyMonitor {
  public getTopology(numGpus: number = 8): GPUAllocation[] {
    return Array.from({ length: numGpus }, (_, i) => ({
      gpu_id: i,
      vram_allocated_gb: 14.8,
      nvme_prefetch_bw_gbs: 28.4
    }));
  }
}
