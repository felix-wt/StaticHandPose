import cv2
def show_optical_flow(prvs):
    prvs = cv2.cvtColor(prvs, cv2.COLOR_BGR2GRAY)
    next = cv2.cvtColor(next, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prev=prvs, next=next, flow=None, pyr_scale=0.5, levels=5,
                                                winsize=15,
                                                iterations=3, poly_n=3, poly_sigma=1.2,
                                                flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
    prvs = cv2.cvtColor(prvs, cv2.COLOR_BGR2GRAY)
    next = cv2.cvtColor(next, cv2.COLOR_BGR2GRAY)
    inst = cv2.optflow.createOptFlow_DeepFlow()
    flow = inst.calc(prvs, next, None)
    flow = cv2.optflow.calcOpticalFlowSF(prvs, next, 2, 2, 4)
    flow = cv2.optflow.calcOpticalFlowSparseToDense(prvs, next)
    inst = cv2.optflow.createOptFlow_PCAFlow()
    flow = inst.calc(prvs, next, None)
    prvs = cv2.cvtColor(prvs, cv2.COLOR_BGR2GRAY)
    next = cv2.cvtColor(next, cv2.COLOR_BGR2GRAY)
    inst = cv2.optflow.createOptFlow_DIS(cv2.optflow.DISOPTICAL_FLOW_PRESET_MEDIUM)
    inst.setUseSpatialPropagation(True)
    flow = inst.calc(prvs, next, None)
    return flow


