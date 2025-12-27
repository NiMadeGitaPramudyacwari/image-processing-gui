classdef app1 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure                matlab.ui.Figure
        ResetButton             matlab.ui.control.Button
        KategoriButtonGroup     matlab.ui.container.ButtonGroup
        NegatifButton           matlab.ui.control.RadioButton
        BinaryButton            matlab.ui.control.RadioButton
        GrayscaleButton         matlab.ui.control.RadioButton
        BrowserImageButton      matlab.ui.control.Button
        NegativeInversionPanel  matlab.ui.container.Panel
        UIAxes_2                matlab.ui.control.UIAxes
        UIAxes                  matlab.ui.control.UIAxes
    end

    
    properties (Access = private)
       originalImage = [] 
    end
    

    % Callbacks that handle component events
    methods (Access = private)

        % Button pushed function: BrowserImageButton
        function BrowserImageButtonPushed(app, ~)
            [fileName, filePath] = uigetfile({'*.jpg;*.png;*.bmp', ...
             'Supported Image Files'}, 'Pilih Gambar');

        if isequal(fileName,0)
                return;
         end

        img = imread(fullfile(filePath, fileName));
        app.originalImage = img;
    
        imshow(img, 'Parent', app.UIAxes);
        title(app.UIAxes, 'Original Image');
    
        cla(app.UIAxes_2);
        end

        % Selection changed function: KategoriButtonGroup
        function KategoriButtonGroupSelectionChanged(app, ~)

            if isempty(app.originalImage)
                uialert(app.UIFigure,'Silakan pilih gambar terlebih dahulu');
                return;
            end

            img = app.originalImage;

            % RGB → Grayscale
            if size(img,3) == 3
                imgGray = rgb2gray(img);
            else
                imgGray = img;
            end

            selected = app.KategoriButtonGroup.SelectedObject.Text;

            switch selected
                case 'Grayscale'
                    result = imgGray;

                case 'Binary'
                    result = imbinarize(imgGray);

                case 'Negatif'
                    result = imcomplement(imgGray);
            end

            imshow(result, 'Parent', app.UIAxes_2);
            title(app.UIAxes_2, ['Hasil: ' selected]);
        end

        % Button pushed function: ResetButton
        function ResetButtonPushed(app, ~)
        cla(app.UIAxes);
        cla(app.UIAxes_2);
        app.originalImage = [];

        % Reset radio button
        app.GrayscaleButton.Value = true;
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.Position = [100 100 640 480];
            app.UIFigure.Name = 'MATLAB App';

            % Create UIAxes
            app.UIAxes = uiaxes(app.UIFigure);
            title(app.UIAxes, 'Original Image')
            xlabel(app.UIAxes, 'X')
            ylabel(app.UIAxes, 'Y')
            zlabel(app.UIAxes, 'Z')
            app.UIAxes.Position = [325 254 244 140];

            % Create UIAxes_2
            app.UIAxes_2 = uiaxes(app.UIFigure);
            title(app.UIAxes_2, 'Compliment Image')
            xlabel(app.UIAxes_2, 'X')
            ylabel(app.UIAxes_2, 'Y')
            zlabel(app.UIAxes_2, 'Z')
            app.UIAxes_2.Position = [325 88 244 140];

            % Create NegativeInversionPanel
            app.NegativeInversionPanel = uipanel(app.UIFigure);
            app.NegativeInversionPanel.TitlePosition = 'centertop';
            app.NegativeInversionPanel.Title = 'Negative (Inversion)';
            app.NegativeInversionPanel.FontWeight = 'bold';
            app.NegativeInversionPanel.FontSize = 18;
            app.NegativeInversionPanel.Position = [68 428 526 30];

            % Create BrowserImageButton
            app.BrowserImageButton = uibutton(app.UIFigure, 'push');
            app.BrowserImageButton.ButtonPushedFcn = createCallbackFcn(app, @BrowserImageButtonPushed, true);
            app.BrowserImageButton.Position = [59 351 161 31];
            app.BrowserImageButton.Text = 'Browser Image';

            % Create KategoriButtonGroup
            app.KategoriButtonGroup = uibuttongroup(app.UIFigure);
            app.KategoriButtonGroup.SelectionChangedFcn = createCallbackFcn(app, @KategoriButtonGroupSelectionChanged, true);
            app.KategoriButtonGroup.Title = 'Kategori';
            app.KategoriButtonGroup.Position = [59 167 161 168];

            % Create GrayscaleButton
            app.GrayscaleButton = uiradiobutton(app.KategoriButtonGroup);
            app.GrayscaleButton.Text = 'Grayscale';
            app.GrayscaleButton.Position = [11 122 76 22];
            app.GrayscaleButton.Value = true;

            % Create BinaryButton
            app.BinaryButton = uiradiobutton(app.KategoriButtonGroup);
            app.BinaryButton.Text = 'Binary';
            app.BinaryButton.Position = [11 100 65 22];

            % Create NegatifButton
            app.NegatifButton = uiradiobutton(app.KategoriButtonGroup);
            app.NegatifButton.Text = 'Negatif';
            app.NegatifButton.Position = [11 78 65 22];

            % Create ResetButton
            app.ResetButton = uibutton(app.UIFigure, 'push');
            app.ResetButton.ButtonPushedFcn = createCallbackFcn(app, @ResetButtonPushed, true);
            app.ResetButton.Position = [59 117 161 37];
            app.ResetButton.Text = 'Reset';

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = app1

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end