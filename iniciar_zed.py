import pyzed.sl as sl
import cv2

def capture_image_and_gps():
    zed = sl.Camera()

    # Define os parâmetros de inicialização
    init_params = sl.InitParameters()
    # forçar o uso da cpu, caso tenha gpu --> apague a linha abaixo
    init_params.sdk_gpu_id = -1 
    init_params.camera_resolution = sl.RESOLUTION.HD1080  # Resolução HD1080
    init_params.camera_fps = 30  # FPS de 30
    init_params.depth_mode = sl.DEPTH_MODE.NONE  # Sem profundidade para simplificação
    init_params.coordinate_units = sl.UNIT.METER  # Coordenadas em metros

    # Abre a câmera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print(f"Erro ao abrir a câmera: {err}")
        return None

    # Captura a imagem da câmera
    image = sl.Mat()
    if zed.grab() == sl.ERROR_CODE.SUCCESS:
        # Converte a imagem para o formato OpenCV
        zed.retrieve_image(image, sl.VIEW.LEFT) 
        image_ocv = image.get_data()  # Extrai os dados da imagem
    else:
        print("Erro ao capturar imagem.")
        image_ocv = None

    # Coleta dados de GPS
    sensors_data = sl.SensorsData()
    if zed.get_sensors_data(sensors_data, sl.TIME_REFERENCE.CURRENT) == sl.ERROR_CODE.SUCCESS:
        gps_data = sensors_data.gnss_data  # Acessa os dados do GPS
        if gps_data.is_available:
            latitude = gps_data.latitude_deg
            longitude = gps_data.longitude_deg
            altitude = gps_data.altitude
            print(f"Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}")
        else:
            print("Dados de GPS não disponíveis")
    else:
        print("Erro ao coletar dados de GPS.")

    zed.close()
    return image_ocv

if __name__ == "__main__":
    image = capture_image_and_gps()
    if image is not None:
        cv2.imshow("ZED Camera", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


