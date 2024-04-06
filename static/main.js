document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('submit-btn').addEventListener('click', function () {
        const feature = document.getElementById('feature-selection').value;
        const startDate = document.getElementById('start-date').value;
        const endDate = document.getElementById('end-date').value;

        // 注意：后端API需要根据传入的特征动态生成图表
        const chartUrl = `http://localhost:5000/api/chart?feature=${feature}&start=${startDate}&end=${endDate}`;


        // document.getElementById('myChart').innerHTML = `<img src="${chartUrl}" alt="Feature Chart">`;
        // 设置图像样式以居中显示并适应其容器的宽度
        document.getElementById('myChart').innerHTML = `<img src="${chartUrl}" alt="Feature Chart" style="max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">`;
    });
});
