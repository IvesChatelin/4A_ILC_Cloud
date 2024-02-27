import { ApplicationConfig} from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { AuthService } from './service/auth.service';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { TweetService } from './service/tweet.service';

export const appConfig: ApplicationConfig = {
  providers: [AuthService, TweetService, provideHttpClient(withFetch()), provideRouter(routes)],
};
